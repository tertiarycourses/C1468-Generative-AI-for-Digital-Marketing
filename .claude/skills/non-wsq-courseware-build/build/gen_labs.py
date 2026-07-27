#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Generate the labs/ markdown from the SAME single source as the deck/LP/LG
(course_data.py + data_domainN.py), so labs stay 100% aligned with the other
artifacts. Emits labs/lab-NN-*.md and labs/README.md (tools.md and the brief
pack are hand-authored). Enrichment sections (Prerequisites, Troubleshooting,
Challenge, Reflection, Deliverable) live in the ENRICH table below, keyed by lab
number. The lab's day is derived from the SCHEDULE so a multi-day course labels
each lab with the correct day.

Run:  python gen_labs.py
"""
import os, re, sys, glob, importlib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C


def find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(start))


REPO = find_repo(HERE)
LABS = os.path.join(REPO, "labs")

# ------------------------------------------------------------------ load labs
DOMS = []
for f in sorted(glob.glob(os.path.join(HERE, "data_domain[0-9]*.py"))):
    mod = importlib.import_module(os.path.splitext(os.path.basename(f))[0])
    key = [k for k in dir(mod) if k.startswith("DOMAIN")][0]
    DOMS.append((getattr(mod, key), getattr(mod, "SCENARIO", None)))

LABSLIST = []
SCENARIO = None
for dom, scen in DOMS:
    if scen and not SCENARIO:
        SCENARIO = scen
    LABSLIST.extend(dom)

TOPIC_TITLE = {t["num"]: t["title"] for t in C.TOPICS}

# ------------------------------------------------------------------ per-lab minutes + day
# Derived from the schedule lab blocks so labs match the Lesson Plan timing and
# each lab shows the correct day.
def _sched():
    return C.SCHEDULE(lambda nums: "\x00".join(str(n) for n in nums))


def approx_minutes_and_day():
    mins, day_of = {}, {}
    for day, (_theme, rows) in _sched().items():
        for row in rows:
            if row[3] == "lab":
                nums = [int(x) for x in row[4].split("Hands-on: ")[-1].split("\x00")]
                per = round(row[2] / len(nums))
                for n in nums:
                    mins[n] = per
                    day_of[n] = day
    return mins, day_of


MINS, DAY_OF = approx_minutes_and_day()

# ------------------------------------------------------------------ per-lab enrichment
ENRICH = {
 1: dict(
    prereqs=[
        "A laptop with a modern web browser (Chrome, Edge, Safari or Firefox) and a reliable internet connection.",
        "An account for at least one chat assistant (ChatGPT, Claude, Gemini or Copilot) and one AI image tool.",
        "The supplied Kopi Culture Co. brief to hand (labs/reference-pack/).",
    ],
    trouble=[
        "**A tool won't let you sign in or generate.** Try a different one — you only need one chat assistant and one image tool to follow the labs; tell the trainer what you have.",
        "**The AI image looks strange or has odd details.** That's expected from a one-line prompt — it's only a warm-up; you make real, on-brand images from proper prompts in Lab 7.",
        "**The two assistants give very different answers.** That's normal — they differ in ideas and range; the prompting and review skills you learn work across all of them.",
    ],
    challenge="Ask a third assistant the same campaign-ideas prompt and rank the three answers — which was most useful for a small brand, and why?",
    lo=1,
    deliverable="Keep your KCC-Neighbourhood-Series folder with your toolkit notes and the brief — it is the home for everything you build across the next labs.",
 ),
 2: dict(
    prereqs=[
        "Completed Lab 1 (your tools are set up and responding).",
        "The supplied Kopi Culture Co. brief open (labs/reference-pack/).",
    ],
    trouble=[
        "**The AI's draft is generic and clichéd.** Add a role and real context (brand, audience, goal, channel); a vague prompt always gives generic copy.",
        "**The AI invents awards or claims.** Tell it explicitly not to invent claims and to stay within the brief — you own every claim you publish.",
        "**The reply is the wrong length or format.** State the format you want (three options, a word limit, a numbered list) as a constraint and regenerate.",
    ],
    challenge="Write a structured prompt for a completely different campaign of your own using the same five parts, proving the template travels beyond the Neighbourhood Series.",
    lo=2,
    deliverable="Keep your reusable marketing prompt library — you run its templates for research, copy, captions, subject lines, image briefs and analysis in every later lab.",
 ),
 3: dict(
    prereqs=[
        "Completed Lab 2 (you can write structured marketing prompts).",
        "The supplied Kopi Culture Co. brief with the brand and voice notes to hand.",
    ],
    trouble=[
        "**The voice sounds generic.** Give the AI more specific brand cues (small-batch, proudly local, witty, knows its coffee) and reject any attribute that could describe any brand.",
        "**The personas feel interchangeable.** Ask the AI to sharpen the differences — different goals, channels and language — until each persona is clearly a different person.",
        "**A rewrite still sounds off.** Tell the AI exactly what is wrong ('too corporate', 'not local enough') rather than just 'try again'.",
    ],
    challenge="Take a coffee brand you admire, describe its voice in three attributes, and note how Kopi Culture Co.'s voice should be different.",
    lo=3,
    deliverable="Keep your brand voice guide and three personas — every later lab holds its content and targeting to them, so the whole campaign sounds like one brand and speaks to real customers.",
 ),
 4: dict(
    prereqs=[
        "Completed Lab 3 (you have a defined brand voice and personas).",
        "Access to the AI image tool you plan to use, and your voice guide to hand.",
    ],
    trouble=[
        "**The checklist is vague.** Ask for plain-language, one-line rules with a concrete example of each risk, not abstract principles.",
        "**The AI states a statistic or award.** Never publish it unverified — the rule is you check or cut every claim; the AI does not know real facts about your brand.",
        "**Disclosure feels awkward.** Decide a simple rule now (for example a light 'made with AI assistance' note where it matters) so you're consistent all course.",
    ],
    challenge="Find one real news example of AI marketing going wrong (a false claim or a data-privacy issue) and note the one rule that would have prevented it.",
    lo=4,
    deliverable="Keep your first campaign ideas, copy and image plus your responsible-generation checklist — the ground rules that keep every later deliverable accurate, original and safe to publish.",
 ),
 5: dict(
    prereqs=[
        "Completed Lab 4 (your responsible-generation rules are set).",
        "Your brand voice guide and personas from Lab 3 to paste into the assistant.",
    ],
    trouble=[
        "**The captions are full of clichés.** Ban the specific clichés in the prompt ('game-changer', 'must-try') and ask for more specific, on-voice lines.",
        "**Every post sounds the same.** Ask for a range of angles (origin, gifting, flavour, convenience) so you have real variety across the calendar.",
        "**The platform versions feel identical.** Remind the AI how Instagram and TikTok differ (polished vs fast/casual) and ask it to change tone, length and format only.",
    ],
    challenge="Write a hook so strong it works with no caption at all — often the sharpest test of a scroll-stopping first line.",
    lo=5,
    deliverable="Keep your social posts, platform variants and two-week content calendar — the social layer you plan and optimise on Day 2.",
 ),
 6: dict(
    prereqs=[
        "Completed Lab 5 (you have social content and a calendar).",
        "Your voice guide and the responsible-use rules from Lab 4 to hand.",
    ],
    trouble=[
        "**The ad copy is over the character limit.** Ask the AI to rewrite to the exact limit (40 characters for a headline) — concise is also stronger.",
        "**The email buries the call to action.** Ask for one clear CTA and move it up; every email should make the next step obvious.",
        "**The subject line feels like clickbait.** Ask for honest, specific subject lines that match the email — clickbait costs you trust and deliverability.",
    ],
    challenge="Write a second launch-email subject line built on curiosity and a third built on a clear benefit, and predict which your audience opens more.",
    lo=6,
    deliverable="Keep your Meta and Google ad variations and your launch and welcome emails — the paid and email layers you personalise, scale and test on Day 2.",
 ),
 7: dict(
    prereqs=[
        "Completed Lab 6 (you know the message each visual must support).",
        "An AI image tool and access to an AI video feature (Canva, Gemini/Veo or a text-to-video tool).",
    ],
    trouble=[
        "**The image is off-brand.** Add style, mood and palette words from your moodboard to the prompt and regenerate; keep every image in the same look.",
        "**The image has garbled text or a fake logo.** Prompt 'no text, no logos' and regenerate; AI image text is unreliable — add real text on the design instead.",
        "**The video clip looks generic.** Tighten the script's hook and beats and feed the AI tool your own images; a strong script matters more than the tool.",
    ],
    challenge="Generate the hero shot in a completely different style (say, flat illustration instead of photography) and decide which better fits Kopi Culture Co.",
    lo=7,
    deliverable="Keep your moodboard, on-brand images and short-form video script and clip (with their prompts) — the visual layer of your campaign.",
 ),
 8: dict(
    prereqs=[
        "Completed Labs 5-7 (you have social, ad, email and visual content).",
        "Your brand voice guide from Lab 3 to run the consistency pass against.",
    ],
    trouble=[
        "**The consistency pass misses things.** Give it your voice guide and ask it to check specific elements (product names, the CTA, key phrases), not just 'make it consistent'.",
        "**Repurposed pieces drift off-message.** Remind the AI to keep the core message and CTA and change only tone, length and format for the channel.",
        "**Product or campaign names vary.** Lock the exact spellings once (the four coffee names, Neighbourhood Series, The KCC Club) and apply them everywhere.",
    ],
    challenge="Repurpose your core piece into one more channel you haven't used (say, a WhatsApp broadcast or a Google Business post) using the same one-to-many workflow.",
    lo=8,
    deliverable="Keep your consistency report, the rewritten pieces and the repurposed one-to-many set — your Day 1 content kit, aligned and ready to plan and optimise.",
 ),
 9: dict(
    prereqs=[
        "Completed Day 1 (you have the content kit, voice and personas).",
        "Any chat assistant open; optionally a real keyword tool to verify volumes.",
    ],
    trouble=[
        "**The persona research feels generic.** Ask for concrete Singapore-specific detail — real buying moments, real channels, exact phrases — and reject anything that could describe anyone.",
        "**The keywords are all broad head terms.** Ask for longer, specific phrases (long-tail) and by intent — they convert better and are easier for a small brand to rank for.",
        "**You can't tell informational from transactional.** Ask the AI to label intent and explain each in one line, then map informational to blog/SEO and transactional to paid.",
    ],
    challenge="Pick one transactional keyword cluster and draft the landing-page headline and meta description it should rank for.",
    lo=9,
    deliverable="Keep your deepened personas, objection-handling messages and clustered keyword map — the research that grounds the campaign plan in Lab 10.",
 ),
 10: dict(
    prereqs=[
        "Completed Lab 9 (you have audience and keyword research).",
        "Your Day 1 content kit and content calendar to hand.",
    ],
    trouble=[
        "**The plan is a list of posts, not a funnel.** Ask the AI to map every content type to a funnel stage and a persona so the plan has structure and purpose.",
        "**The channel mix over-spends.** Push the budget toward organic social, email and SEO; ask the AI to justify any paid spend and flag what to hold off on.",
        "**The timeline is unrealistic for a small team.** Ask for a lean week-by-week plan and cut anything that can't ship — a runnable plan beats an ambitious one.",
    ],
    challenge="Add a single 'if this works, double down here' contingency to your plan — naming the metric that would trigger it.",
    lo=10,
    deliverable="Keep your objectives, funnel map, channel mix and launch timeline — the Neighbourhood Series campaign plan you personalise, scale and optimise next.",
 ),
 11: dict(
    prereqs=[
        "Completed Lab 10 (you have a multi-channel campaign plan).",
        "Your personas and core offer/launch message to hand.",
    ],
    trouble=[
        "**The personalised versions lose the core message.** Remind the AI to keep the message, offer and voice and change only framing, benefit and CTA per persona.",
        "**The scaled variants feel repetitive.** Ask for genuinely different angles per variant, then cut any that are near-duplicates — variety, not volume, is the point.",
        "**A variant drifts off voice.** Run every scaled variant back through the voice guide in one pass and fix what drifted before you use it.",
    ],
    challenge="Personalise one piece for a fourth micro-segment you invent (say, corporate gifting for offices) and note how framing and CTA shift.",
    lo=11,
    deliverable="Keep your personalised offer, segmented emails, per-audience ad set and caption variants with the segment-to-variant mapping — the content you A/B test in Lab 12.",
 ),
 12: dict(
    prereqs=[
        "Completed Lab 11 (you have personalised, scaled content).",
        "Any chat assistant open.",
    ],
    trouble=[
        "**The two variants aren't really different.** A test needs a meaningful difference in one element — ask the AI for genuinely distinct A and B, not reworded twins.",
        "**You're testing too many things at once.** Change one element per test with one deciding metric, or you won't know what caused the result.",
        "**The result looks decisive but the sample is tiny.** Note that small samples can mislead; confirm the difference holds before you roll it out.",
    ],
    challenge="Design a test where you genuinely can't predict the winner — those are the tests that teach you the most about your audience.",
    lo=12,
    deliverable="Keep your A/B test designs, the worked interpretation and your next-round plan — the optimisation habit that carries into the analytics work.",
 ),
 13: dict(
    prereqs=[
        "Completed Lab 12 (you have tested content and an optimisation habit).",
        "The sample metrics table (or your own non-confidential sample) to hand.",
    ],
    trouble=[
        "**The analysis is a generic summary.** Ask focused questions ('which channel has the best CPA and why') so the answer is actionable, not a restatement of the numbers.",
        "**The AI invents a figure or trend.** Always check its reading against the source table; correct anything that doesn't match before you act.",
        "**You're tempted to paste real data.** Don't — use only anonymised or sample data in a public tool; never real customer lists or confidential revenue.",
    ],
    challenge="Add one more channel row with numbers you make up, and see whether the AI's 'best channel' verdict still matches what the numbers actually say.",
    lo=13,
    deliverable="Keep your verified performance analysis, the diagnosis and the data-tied next actions — the insights that feed the stakeholder report.",
 ),
 14: dict(
    prereqs=[
        "Completed Lab 13 (you know what the campaign needs to improve).",
        "Any chat assistant open; optionally a Zapier/Make or custom-GPT account to explore.",
    ],
    trouble=[
        "**The automation has no safety net.** Add a human review point before anything publishes — a small brand should never auto-post unreviewed AI content.",
        "**The workflow is vague.** Ask for a numbered flow with a clear trigger, the exact AI prompt, and the review and brand checks named explicitly.",
        "**It risks brand or accuracy drift.** Build in a voice-and-accuracy check step and list what data must never enter the tool.",
    ],
    challenge="Sketch a second automation for a different task (weekly performance summary) and decide which of the two saves more time for less risk.",
    lo=14,
    deliverable="Keep your automation blueprint, guardrails and build notes — the workflow-automation layer of your playbook.",
 ),
 15: dict(
    prereqs=[
        "Completed Lab 13 (you have a verified performance analysis).",
        "Any chat assistant open.",
    ],
    trouble=[
        "**The report is a data dump.** Ask for an executive summary, plain-language meaning and recommendations — a report is a story for a decision-maker, not a table.",
        "**The recommendations are generic.** Push each into a concrete, data-justified action; reject anything the numbers don't support.",
        "**The narrative overclaims.** Hold it to your verified analysis — the report must match what the data actually showed.",
    ],
    challenge="Rewrite your executive summary as three bullet points a busy owner could read in ten seconds and still act on.",
    lo=15,
    deliverable="Keep your one-page report, the lead insight and recommendation, and the reusable monthly reporting template — the reporting layer of your playbook.",
 ),
 16: dict(
    prereqs=[
        "Completed Labs 1-15 (you have every deliverable to assemble).",
        "Somewhere you can rehearse the presentation aloud.",
    ],
    trouble=[
        "**The playbook is just a pile of files.** Give it a clear structure and a 'how to use this' intro so a teammate could actually run the next campaign from it.",
        "**A section points to nothing.** Make sure each section links to the real prompt or asset you created; note any gap to fill later.",
        "**The pitch is a description, not a story.** Open with the opportunity and the idea, then the plan and the early results — lead with the hook, not the brand history.",
    ],
    challenge="Record yourself delivering the five-minute pitch once, then ask the AI to critique a transcript for clarity and filler words.",
    lo=16,
    deliverable="Keep your finished AI Marketing Playbook and the presentation outline — the reusable, pitch-ready campaign the course set out to build.",
 ),
}


def slug(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    if len(s) > 60:
        s = s[:60].rstrip("-")
    return s


def steps_md(steps):
    out = []
    for i, (instr, cmd) in enumerate(steps, 1):
        out.append(f"### Step {i}\n\n{instr}")
        if cmd:
            out.append("Prompt to use (paste into your AI assistant — ChatGPT, Claude, Gemini, Copilot or your image/video tool):\n\n```text\n" + cmd + "\n```")
    return "\n\n".join(out)


def lab_filename(lab):
    return f"lab-{lab['num']:02d}-{slug(lab['title'])}.md"


def build_lab(lab):
    e = ENRICH[lab["num"]]
    topic = lab["topic"]
    mins = MINS.get(lab["num"], 40)
    day = DAY_OF.get(lab["num"], 1)
    parts = []
    parts.append(f"# Lab {lab['num']} — {lab['title']}\n")
    parts.append(
        f"**Topic 0{topic}:** {TOPIC_TITLE[topic]}  |  **Day {day}**  |  "
        f"**Approx. {mins} min**  |  **Course:** {C.TITLE}\n"
    )
    if SCENARIO:
        parts.append("## Scenario\n\n" + SCENARIO + "\n")
    parts.append("## Goal\n\n" + lab["objective"] + "\n")
    parts.append("## What you'll build\n\n" + lab["build"] + "\n")
    parts.append("**Tools and techniques:** " + lab["services"] + "\n")
    parts.append("## Prerequisites\n\n" + "\n".join("- " + p for p in e["prereqs"]) + "\n")
    parts.append("## Steps\n\n" + steps_md(lab["steps"]) + "\n")
    parts.append("## Test it\n\n" + lab["test"] + "\n")
    parts.append("## Troubleshooting\n\n" + "\n".join("- " + t for t in e["trouble"]) + "\n")
    parts.append("## Challenge\n\n" + e["challenge"] + "\n")
    lo = C.LEARNING_OUTCOMES[e["lo"] - 1]
    lo_text = lo.split(":", 1)[1].strip().rstrip(".")
    parts.append(f"## Reflection\n\nLO{e['lo']} — In your own words: {lo_text}?\n")
    parts.append("## Deliverable\n\n" + e["deliverable"] + "\n")
    parts.append("---\n")
    parts.append(
        f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · © 2026 {C.ORG}*"
    )
    return "\n".join(parts) + "\n"


def build_readme(files):
    rows = []
    for lab in LABSLIST:
        fn = files[lab["num"]]
        day = DAY_OF.get(lab["num"], 1)
        rows.append(
            f"| {day} | 0{lab['topic']} | {lab['num']:02d} | [{lab['title']}]({fn}) |"
        )
    md = []
    md.append(f"# Labs — {C.TITLE}\n")
    md.append(f"**Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**\n")
    md.append(
        "All 16 labs build one connected **Neighbourhood Series launch campaign** for the fictional Singapore "
        "specialty-coffee brand **Kopi Culture Co.**, which you begin in Lab 1 and finish in Lab 16 — from a "
        "blank page, through ChatGPT, Claude, Gemini and Copilot for research, voice, personas, copy, plan and "
        "analysis, and AI image and video tools for on-brand visuals, out to a planned, personalised, tested, "
        "measured and automated multi-channel campaign, and finally a reusable **AI Marketing Playbook**. A Kopi "
        "Culture Co. brief with the brand facts you need is supplied in `reference-pack/`; use your own "
        "non-confidential brand or product wherever you prefer. There is **no assessment** — each lab verifies "
        "itself with a 'Test it' step.\n"
    )
    md.append("| Day | Topic | Lab | Title |")
    md.append("|---:|---|---:|---|")
    md.extend(rows)
    md.append("")
    md.append("## Tools\n")
    md.append("See [tools.md](tools.md) for the accounts and tools used across the labs, and "
              "[reference-pack/](reference-pack/) for the Kopi Culture Co. brief.")
    return "\n".join(md) + "\n"


def main():
    os.makedirs(LABS, exist_ok=True)
    for old in glob.glob(os.path.join(LABS, "lab-*.md")):
        os.remove(old)
    files = {}
    for lab in LABSLIST:
        fn = lab_filename(lab)
        files[lab["num"]] = fn
        with open(os.path.join(LABS, fn), "w", encoding="utf-8") as fh:
            fh.write(build_lab(lab))
        print("wrote labs/" + fn)
    with open(os.path.join(LABS, "README.md"), "w", encoding="utf-8") as fh:
        fh.write(build_readme(files))
    print("wrote labs/README.md")


if __name__ == "__main__":
    main()
