# Acceptance criteria — TakeMeter

Five criteria that say what "working" means for this classifier, written in
unit 5 **before** anything was trained.

**All five are yours this time.** None are given. You've had two projects of
practice.

An acceptance criterion names a number. *"The model is accurate"* is an
opinion. *"Every label has an F1 of at least 0.60 on the held-out set"* is a
criterion.

Under each, write a sentence or two on **why that number**. A reason that says
something about your data or your taxonomy earns credit — *"I picked 0.60 F1
for `reaction` because it's my smallest label and I only have about 50
examples of it"*. A reason that could be attached to any project does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## Pick numbers you can defend

Not numbers that sound impressive. Three labels means a coin-flip guesser gets
about 33%, so a target of 0.40 is barely a target. Your number should sit
somewhere you'd honestly call useful.

**Cover at least three of these five areas.** They're here as prompts, not as a
form to fill in — a criterion that fits none of them is fine if it names a
number.

| Area | A question it could answer |
|---|---|
| Overall accuracy | How often does it need to be right to be worth using? |
| Per-label performance | Is one label allowed to be much worse than the others? |
| Balance | How lopsided can your label counts get before it's a problem? |
| Consistency | If someone else labelled the same posts, how often should you agree? |
| Confidence | Should a confident prediction be right more often than an unsure one? |

Two things worth knowing before you pick numbers, because both will affect
whether you hit them:

- **Your smallest label will have the jumpiest score.** If a label has 50
  examples, about 8 land in the test split. An F1 computed on 8 examples moves
  a lot between seeds. A target for that label should be looser than one for
  your biggest label, and saying so is a good reason.
- **Unit 6 tests across three seeds, and the target has to hold across all
  three.** A target of 0.65 against results of 0.71, 0.62, 0.68 is a **miss**.
  Pick with that in mind — it is stricter than it first sounds.

---

## 1.

Held-out test accuracy is at least **0.70**.

**Why this target:** The dataset has four equally sized topic classes, so a
random guesser would be correct about 25% of the time. A 70% target is well
above chance while still allowing for short articles that combine business,
technology, science, and public-affairs vocabulary.


---

## 2.

Macro F1 on the held-out test split is at least **0.68**.

**Why this target:** Macro F1 gives each of the four AG News topics equal
weight. This matters because the 50-per-class sample is intentionally balanced,
so a strong overall score should not hide weak performance on one topic.


---

## 3.

Every label has an F1 score of at least **0.60** on the held-out test split.

**Why this target:** The stratified 70/15/15 split puts only about eight
examples from each 50-example label into the test set, so an individual F1 can
move substantially between seeds. A 0.60 floor is demanding enough to catch a
failed class without treating normal small-test-set variation as failure.


---

## 4.

No label accounts for more than **30%** of `labels.csv`.

**Why this target:** The sample intentionally contains 50 examples in each of
the four source classes, or 25% per label. A 30% cap preserves that balance and
prevents a model from appearing accurate mainly by predicting a majority topic.


---

## 5.

In a 20-article source-label audit, **100%** of the stored labels match the
instructor-approved AG News source labels.

**Why this target:** These labels come from an approved pre-labeled benchmark,
not from a new manual taxonomy. The audit verifies that the four source labels
were transferred and mapped to `world`, `sports`, `business`, and `sci_tech`
without transcription or mapping errors.


---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 6 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath, like this:

         ## 2. Every label performs acceptably

         The model performs well on all labels.

         **Why this target:** ...

         > **Revised in unit 6:** Every label has an F1 of at least 0.60 on
         > the held-out set.
         >
         > **Why revised:** "performs well" gave me nothing to check. I
         > couldn't produce a verdict from it at all.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "Overall accuracy of at least 0.65" → "at least 0.55", because
            0.65 turned out to be optimistic for 200 examples.

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.
     ───────────────────────────────────────────────────────────────────────── -->
