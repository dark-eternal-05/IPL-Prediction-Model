import os, django, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from django.utils.dateparse import parse_datetime

os.environ.setdefault("DJANGO_SETTINGS_MODULE","ipl_project.settings")
django.setup()

from .models import Team, Match, Player, PlayerPerformance
from .ml_utils import broadcast_update

def setup_driver():
    opts=Options(); opts.add_argument("--headless")
    return webdriver.Chrome(options=opts)

def run_scraper():
    driver=setup_driver()
    driver.get("https://www.espncricinfo.com/series/ipl-2025-1382490/match-results")
    time.sleep(5)
    links=driver.find_elements(By.XPATH,"//a[contains(@href,'full-scorecard')]")
    for url in [links[0].get_attribute("href")]:
        driver.get(url); time.sleep(5)
        teams=driver.find_elements(By.CLASS_NAME,"ds-text-tight-l")
        a,b=teams[0].text,teams[1].text
        team_a, _=Team.objects.get_or_create(name=a, defaults={"short_code":a[:3].upper()})
        team_b, _=Team.objects.get_or_create(name=b, defaults={"short_code":b[:3].upper()})
        sid=url.split("/")[-2]
        mdate=parse_datetime(time.strftime("%Y-%m-%dT%H:%M:%S"))
        s=driver.find_elements(By.CLASS_NAME,"ds-text-compact-m")[0].text
        sa=int(s.split("/")[0]); sb=int(driver.find_elements(By.CLASS_NAME,"ds-text-compact-m")[1].text.split("/")[0])
        match, _=Match.objects.update_or_create(match_id=sid, defaults={
            "date":mdate,"team_a":team_a,"team_b":team_b,
            "team_a_score":sa,"team_b_score":sb,
            "winner": team_a if sa>sb else team_b
        })
        rows=driver.find_elements(By.CSS_SELECTOR,"tbody tr")[:5]
        for r in rows:
            cols=r.find_elements(By.TAG_NAME,"td")
            name=cols[0].text; runs=int(cols[2].text)
            p,_=Player.objects.get_or_create(name=name, team=team_a)
            PlayerPerformance.objects.update_or_create(player=p,match=match,defaults={"runs":runs})
        broadcast_update({
            "match_id":sid,"team_a_score":sa,"team_b_score":sb
        })
    driver.quit()
