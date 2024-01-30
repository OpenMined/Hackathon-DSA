from pathlib import Path
from langchain_community.document_loaders import DirectoryLoader, TextLoader

DATA_DIR = Path(__file__).parent.parent / "data"
SNAPSHOTS_DIR = DATA_DIR / "platform-docs-snapshots"
VERSIONS_DIR = DATA_DIR / "platform-docs-versions"
DECLARATIONS_DIR = DATA_DIR / "platforms-doc-declarations"
TRAIN_DIR = DATA_DIR / "challenge-2-dataset-and-documentation" / "dataset" / "train"

SAMPLES_FROM_SLIDES = [
    (
        "How is content moderation carried out on X?",
        "Content moderation on X combines automatic approaches and human evaluators. According to their transparency report, X uses heuristic and automatic models (automatic language processing, computer vision, etc.) to detect potentially prohibited content. Human moderators are then responsible for verifying that the detected content is indeed prohibited. The combination of human moderators and algorithms is also used to evaluate and improve moderation models.",
    ),
    (
        "I'm a sociology researcher with expertise in social networks. How can I study advertising on LinkedIn?",
        "The LinkedIn Ad Library lets you search for ads published on LinkedIn. They are available for one year. No account is required. Ads are available between 24 and 48 hours after their first display. It is not possible to search for specific advertising partnerships between a brand and a LinkedIn creator.",
    ),
    (
        "How many Italian government data requests did LinkedIn receive in 2022? Please provide the URL of the source.",
        "LinkedIn received 45 data requests from the Italian government in 2022: 11 between January and June, and 34 between July and December. This information is available at https://about.linkedin.com/transparency/government-requests-report.",
    ),
    (
        "Write me a curl request. This query should allow me to obtain from Facebook all political ads containing the word 'europe' that have reached France and Belgium. The response should only contain the curl request code.",
        "curl -G -d 'search_terms='europe'' -d 'ad_type=POLITICAL_AND_ISSUE_ADS' -d 'ad_reached_countries=['FR','BE']' -d 'access_token=<ACCESS_TOKEN>' 'https://graph.facebook.com/<API_VERSION>/ads_archive'",
    ),
]


def get_version_files():
    return VERSIONS_DIR.glob("[!.]*/[!.]*.md")


def load_versions_files():
    docs = DirectoryLoader(
        VERSIONS_DIR, glob="[!.]*/[!.]*.md", loader_cls=TextLoader
    ).load()
    docs = [d for d in docs if Path(d.metadata["source"]) != VERSIONS_DIR / "README.md"]
    return docs


def get_training_data():
    questions_file = TRAIN_DIR / "input" / "questions.csv"

    with open(questions_file, "r") as f:
        questions = [line.strip().split(";") for line in f.readlines()[1:]]
    questions = {int(q[0]): q[1] for q in questions}

    answers_dir = TRAIN_DIR / "output" / "answers"
    answers = {}
    for p in answers_dir.glob("**/*.txt"):
        idx = int(p.stem[:3])
        with open(p, "r") as f:
            answer = f.read()
        if idx not in answers:
            answers[idx] = []
        answers[idx].append(answer)

    sources_dir = TRAIN_DIR / "output" / "sources"
    sources = {}
    for p in sources_dir.glob("*.txt"):
        with open(p, "r") as f:
            sources[int(p.stem)] = f.read().strip()

    idx = list(questions.keys())
    idx.sort()
    questions = [questions[i] for i in idx]
    answers = [answers[i] for i in idx]
    sources = [sources[i] for i in idx]
    return questions, answers, sources
