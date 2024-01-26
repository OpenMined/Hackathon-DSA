from pathlib import Path

DATA_DIR = Path(__file__).parent / "data"
SNAPSHOTS_DIR = DATA_DIR / "platform-docs-snapshots"
VERSIONS_DIR = DATA_DIR / "platform-docs-versions"

SAMPLE_QA = [
    ("How is content moderation carried out on X?", 
     "Content moderation on X combines automatic approaches and human evaluators. According to their transparency report, X uses heuristic and automatic models (automatic language processing, computer vision, etc.) to detect potentially prohibited content. Human moderators are then responsible for verifying that the detected content is indeed prohibited. The combination of human moderators and algorithms is also used to evaluate and improve moderation models."),
    
    ("I'm a sociology researcher with expertise in social networks. How can I study advertising on LinkedIn?", 
     "The LinkedIn Ad Library lets you search for ads published on LinkedIn. They are available for one year. No account is required. Ads are available between 24 and 48 hours after their first display. It is not possible to search for specific advertising partnerships between a brand and a LinkedIn creator."),
    
    ("How many Italian government data requests did LinkedIn receive in 2022? Please provide the URL of the source.", 
     "LinkedIn received 45 data requests from the Italian government in 2022: 11 between January and June, and 34 between July and December. This information is available at https://about.linkedin.com/transparency/government-requests-report."),
    
    ("Write me a curl request. This query should allow me to obtain from Facebook all political ads containing the word 'europe' that have reached France and Belgium. The response should only contain the curl request code.", 
     "curl -G -d 'search_terms='europe'' -d 'ad_type=POLITICAL_AND_ISSUE_ADS' -d 'ad_reached_countries=['FR','BE']' -d 'access_token=<ACCESS_TOKEN>' 'https://graph.facebook.com/<API_VERSION>/ads_archive'")
]

def get_version_files():
    return VERSIONS_DIR.glob("[!.]*/[!.]*.md")
