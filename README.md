# TakeMeter

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, the
> notebook, the baseline, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> head -5 data/practice_labels.csv     # the shape your labels.csv needs
> ```
>
> Then open `takemeter.ipynb` **in this folder** — in VS Code, or with
> `jupyter notebook` if you prefer. Pick the kernel: the `.venv` inside this
> project. Run section 1, which reports the hardware you'll be training on.
> Everything else waits until you have data.
>
> Nothing to upload, nothing to connect, no accounts and no keys. The notebook
> runs on your machine and writes next to your code.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     Unit 5 asks for the first five sections. Unit 6 adds the five below them.

     Everything is pasted as TEXT. No screenshots, no images.

     ⚠️ The confusion matrix especially. The notebook prints one as a markdown
     table, ready to copy. A screenshot of a matrix earns nothing. Paste the
     table.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 5 — THE BUILD ═══════════════════════ -->

## What This Does

<!-- Your community, and what your classifier sorts posts into. Three or four
     sentences. -->

This classifier sorts short news articles from the instructor-approved AG News
dataset into four source topics: `world`, `sports`, `business`, and `sci_tech`.
It uses a balanced sample of 200 articles, with 50 articles in each class.
The dataset's original labels are retained and disclosed in every `note` cell.

**Repository URL:** https://github.com/abelmechal/ai201-project3-takemeter-starter-v2026


---

## Label Taxonomy

<!-- Each label: a one-sentence definition and two real examples from your
     reading. Then your decision rule for the hardest boundary.

     The decision rule is worth a point on its own and it's the thing most
     people leave out. Every taxonomy has a hardest boundary. Name yours. -->

### `world`

**Definition:** News primarily about international events, government,
politics, conflict, crime, or public affairs.

**Example 1:**
> Mexico Lawmakers Protest Education Funding (AP) ... Mexico City legislators
> ... seized the speaker's podium Tuesday to prevent discussion of proposed
> funding changes for local education.

**Example 2:**
> Three appear in Victoria court on drug charges linked to legislature raid
> (Canadian Press) ...

### `sports`

**Definition:** News primarily about sports teams, athletes, competitions, or
sporting events.

**Example 1:**
> Beasley calls out his 49ers for effort ... despite their youth, injuries and
> lousy 1-6 record ...

**Example 2:**
> I'm fully prepared for the Nagpur test: Tendulkar ...

### `business`

**Definition:** News primarily about companies, markets, financial results,
commerce, or economic activity.

**Example 1:**
> FedEx Profit, Outlook Up, Stock Down ... quarterly profit nearly quadrupled
> ... but the stock slipped ...

**Example 2:**
> At least five rigs adrift in the Gulf ... Three others were damaged by
> Hurricane Ivan.

### `sci_tech`

**Definition:** News primarily about science, research, computing,
telecommunications, or technology products and services.

**Example 1:**
> Sport fishermen depleting some saltwater species ... researchers report ...
> nearly a quarter of the catch from overfished species.

**Example 2:**
> Nokia Launches Wireless Content Solution ... Nokia ... launched Monday ...
> a major worldwide initiative.

### The hardest boundary

**Which two labels:** `business` and `sci_tech`

**The decision rule I used every time:** If an article is mainly about a
company's financial result, market activity, or commercial decision, label it
`business`. If it is mainly about a scientific finding, technology product, or
technical development, label it `sci_tech`, even when a company is mentioned.



---

## The Dataset

<!-- Where you collected from, how you labelled, your counts, and three hard
     cases. -->

**Where the posts came from:**

The instructor-approved [AG News dataset](https://huggingface.co/datasets/xwjzds/ag_news),
using its training split. A reproducible random sample selected 50 articles
from each original class.

**How I labelled them:** <!-- Cold first? Pre-labelled with AI and corrected?
Say so plainly — the disclosure is required, not penalised. -->

The source dataset supplied the original topic labels. I mapped `World`,
`Sports`, `Business`, and `Sci/Tech` to `world`, `sports`, `business`, and
`sci_tech`. This pre-labeled-source workflow was approved by the instructor.
Every `note` cell in `labels.csv` identifies the source label.

**Source-label audit:** A deterministic 20-row audit found 20/20 stored labels
matching the original AG News labels. See
[the audit report](data/ag_news_source_label_audit.md).

**Counts per label:**

| Label | Count | Share |
|---|---|---|
| `world` | 50 | 25% |
| `sports` | 50 | 25% |
| `business` | 50 | 25% |
| `sci_tech` | 50 | 25% |
| **Total** | **200** | **100%** |

**Three hard cases**

<!-- Any post that made you pause: what it was, which two labels it could have
     been, and what you chose. These are worth more than the easy 190. -->

**1.**
> *The post:* Nokia Launches Wireless Content Solution ... Nokia described its
> new Preminet solution as a major worldwide initiative.
>
> *Could have been:* `business` or `sci_tech`
>
> *I chose:* `sci_tech`, because the focus is the wireless-content technology
> product, not a financial result or commercial transaction.

**2.**
> *The post:* At least five rigs adrift in the Gulf ... three others were
> damaged by Hurricane Ivan.
>
> *Could have been:* `world` or `business`
>
> *I chose:* `business`, because the article is centered on offshore oil-rig
> operations and the named energy company rather than the broader storm event.

**3.**
> *The post:* Sport fishermen depleting some saltwater species ... researchers
> report that recreational fishing accounts for nearly a quarter of the catch
> from overfished species.
>
> *Could have been:* `sports` or `sci_tech`
>
> *I chose:* `sci_tech`, because it reports a research finding about fish stocks
> rather than a sports competition or athlete.

---

## The Training Run

<!-- Your starting model, your settings, and anything you changed and why. -->

**Base model:** `distilbert-base-uncased`

**Settings:** 3 epochs, learning rate `2e-5`, batch size 16, maximum length
128, seed 42, CPU training.

**Anything I changed from the defaults, and why:** I kept the starter model and
hyperparameters unchanged. The dataset is small and balanced, so the default
settings provided a clear baseline before any future improvement experiment.

**Split sizes:** 139 training articles, 31 validation articles, and 30 test
articles. The test split contains 7 `world`, 8 `sports`, 8 `business`, and 7
`sci_tech` examples. The two labels with seven test examples may have more
variable F1 scores across the three seeds in Unit 6.

**Unit 5 result:** Accuracy was 0.967 and macro F1 was 0.967 on the held-out
test split.



---

## How I Used AI

<!-- Two specific moments — what you asked, what came back, what you changed.

     ⚠️ Plus disclosure of any pre-labelling. If you had a model pre-label a
     batch and then read and corrected every one, say that. It's an allowed
     workflow and disclosing it costs you nothing. Not disclosing it is the
     problem. -->

**Moment 1**

- *What I asked for:* I asked AI to compare possible datasets against the
  TakeMeter requirements.
- *What came back:* It explained that the UCI Zoo dataset was structured data
  with too few rows for this text-classification project, while AG News was a
  text dataset with four existing topic labels.
- *What I changed:* After confirming instructor approval, I used a balanced
  AG News sample instead of the original dataset idea.

**Moment 2**

- *What I asked for:* I asked AI to help create a reproducible dataset sample
  and verify the training setup.
- *What came back:* It created a seed-based sampler, checked that the CSV had
  200 unique rows with 50 per label, aligned the notebook labels with the CSV,
  and reported the Unit 5 metrics.
- *What I changed:* I reviewed the approved label mapping and used the four
  labels `world`, `sports`, `business`, and `sci_tech` in the project files.

**Pre-labelling disclosure:** All 200 labels are instructor-approved source
labels from the AG News benchmark. They were not generated by an AI model for
this project. The original source labels were mapped as follows: `World` to
`world`, `Sports` to `sports`, `Business` to `business`, and `Sci/Tech` to
`sci_tech`.

<!-- ═══════════════════════ UNIT 6 — THE TEST ═══════════════════════

     Don't fill these in during unit 5.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Baseline vs. Trained

<!-- Both models on the same posts. `python baseline.py --trained results.json`
     prints this table for you. -->

| Measure | Baseline | Trained | Difference |
|---|---|---|---|
| Overall accuracy | 1.000 | 0.967 | -0.033 |
| Macro F1 | 1.000 | 0.967 | -0.033 |
| F1 — `business` | 1.000 | 0.933 | -0.067 |
| F1 — `sci_tech` | 1.000 | 1.000 | +0.000 |
| F1 — `sports` | 1.000 | 1.000 | +0.000 |
| F1 — `world` | 1.000 | 0.933 | -0.067 |

**What I predicted before I looked:**
<!-- Milestone 1 asks you to write this BEFORE seeing the trained numbers. A
     prediction made afterwards isn't one. -->

I predict the trained model will outperform the zero-shot baseline overall,
especially on `sports` and `business`, because it was fine-tuned on 200
balanced AG News articles.

**What the gap actually means:**
<!-- If the baseline matched your trained model, your fine-tuning added
     nothing — and that is a real finding, not a failure. Say it plainly. -->

The zero-shot BART baseline outperformed the fine-tuned DistilBERT model by
0.033 on both accuracy and macro F1 on this 30-article held-out split. The
baseline was perfect on all four labels, while the trained model missed one
`business` article and one `world` article. This result does not support my
prediction: with this small balanced AG News sample, the pretrained baseline
generalized better than the fine-tuned model.



---

## Run Log — Before

<!-- Five criteria across three seeds. The notebook's section 6 prints the
     spread table; the Target and Verdict columns are yours. -->

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

### Confusion matrix

<!-- ⚠️ TYPED AS A MARKDOWN TABLE. The notebook prints one ready to paste.
     An image of a matrix earns nothing. -->

| true \ predicted |  |  |  |
|---|---|---|---|
| **** |  |  |  |
| **** |  |  |  |
| **** |  |  |  |

**My biggest off-diagonal number, and what it means:**
<!-- Not "the model made mistakes" — WHICH boundary it didn't learn, and which
     direction. "7 real analysis posts were called hot_take and only 3 went the
     other way" is a direction, not just an error rate. -->



---

## Verdicts and Diagnoses

<!-- MET or MISSED against LAST UNIT's target. The target has to hold across
     all three seeds, not turn up sometimes. -->

| # | Criterion | Target | Verdict | How I decided |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |
| 3 |  |  |  |  |
| 4 |  |  |  |  |
| 5 |  |  |  |  |

**Diagnoses**

<!-- For each miss: the cause, and how you know. The four common causes are:
     too few examples for a label, a boundary you applied inconsistently, a
     genuinely hard label pair, and a task the model can't reach from this
     much data.

     ⚠️ Use your agreement report as evidence. It is the only instrument you
     have that can tell a LABELLING problem from a MODEL problem, and this
     section is graded on whether you used it that way. -->



---

## Agreement Report

<!-- Your rate against the staff set, and every disagreement adjudicated.

     Remember you labelled these 30 under the STAFF taxonomy in
     data/staff_taxonomy.md, not your own — so every argument below is made
     from those definitions and those decision rules. -->

**Agreement rate:** 30 / 30 = 100%

<!-- Nobody grades this number. A 60% who argues every disagreement from the
     stated rules beats a 95% who wrote "staff was right" nine times. Several
     of the 30 were chosen because they're genuinely ambiguous — you should be
     winning some of these. -->

**Disagreements**

<!-- Three lines each: the post, both labels, and who you think is right and
     why — grounded in the staff definitions you were both applying.

     Then sort each into one of three piles:
       (a) the rule covered it and I applied it loosely → a consistency problem
       (b) the rule genuinely doesn't say               → a gap in the definitions
       (c) the rule is ambiguous here and my reading is defensible → argue it.
           This is a legitimate win.

     Pile (a) is the one that matters most for your diagnosis: if you applied a
     written rule two different ways on 30 posts, that is direct evidence about
     what you did across your own 200. -->

None. All 30 independent labels matched the staff answer key, so there were no
disagreements to adjudicate or sort into piles.

**What the pattern in my disagreements tells me:**

There is no disagreement pattern in this 30-post staff sample. The result
suggests I applied the staff definitions and boundary rules consistently on
these examples; it does not prove that every label in my separate AG News
dataset is error-free.


---

## The Improvement

**What I changed:**

**Which diagnosis pointed at it:**

### Run Log — After

| Criterion | Target | Seed 42 | Seed 7 | Seed 2024 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Did it help, and how do I know:**

<!-- If it didn't, say so. Relabelling that didn't help is a genuinely
     interesting result and earns full credit. -->



---

## What's Still Broken

<!-- For each criterion still missed: what you'd do, and why you stopped. -->



**The gap between what I meant my labels to capture and what the model
learned:**
<!-- Two sentences. Your confusion matrix is the evidence. -->



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 5

       [ ] criteria.md has five numbered criteria, each naming a NUMBER
       [ ] Each has a reason underneath tied to your data or taxonomy
       [ ] labels.csv: at least 150 rows, text/label/note, ONE file not split
       [ ] No label above 70%
       [ ] All five unit 5 sections have real content
       [ ] Label Taxonomy includes the decision rule for your hardest boundary
       [ ] The Dataset includes three hard cases
       [ ] results.json and test_split.csv committed (the notebook does this)
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 6

       [ ] Baseline vs. Trained table, with your prediction written beforehand
       [ ] Run Log — Before, five criteria across three seeds
       [ ] Confusion matrix TYPED AS A MARKDOWN TABLE
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, using the agreement report as evidence
       [ ] Agreement Report with every disagreement adjudicated
       [ ] One improvement, with Run Log — After
       [ ] What's Still Broken
       [ ] results_three_seeds_before.json, results_three_seeds_after.json,
           baseline_results.json and
           agreement_results.json committed
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
