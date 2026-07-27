# -*- coding: utf-8 -*-
"""
Domain 4 — Analytics and Workflow with AI. Labs 13-16 (Day 2).

Lab 13 analyses marketing performance with AI; Lab 14 automates a marketing
workflow; Lab 15 turns the data into a stakeholder report; Lab 16 assembles the
reusable AI Marketing Playbook and presents the campaign. Each lab works on the
campaign built across Labs 1-12 and keeps data privacy and verification front of
mind.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Neighbourhood Series campaign and AI "
 "Marketing Playbook, the connected campaign you assemble across all 16 labs."
)

DOMAIN4 = [
 dict(
 num=13, topic=4,
 title="Analyse Marketing Performance with AI",
 objective="Use AI to analyse sample Neighbourhood Series campaign metrics — read the key numbers, diagnose what is underperforming and why, and decide the next action — while verifying the analysis and protecting data privacy.",
 desc="The point of marketing is results, so you close the loop by reading the numbers. In this lab you use a "
 "chat assistant to analyse a realistic set of campaign metrics. You paste in a small sample results table "
 "(impressions, click-through rate, cost per click, cost per acquisition, conversion rate, and email open and "
 "click rates across channels) and ask AI focused questions — which channel has the best cost per acquisition, "
 "what is dragging conversion, where the budget is being wasted — so the answer is actionable rather than a "
 "generic summary. You then have AI propose specific next actions tied to the data, and you sanity-check its "
 "reading against the source numbers, because AI can misread a table or invent a trend. Throughout, you keep "
 "real, confidential customer data out of the public tool and work only with the sample. " + PROJECT_NOTE,
 build="An AI-assisted performance analysis of the sample campaign metrics — the key reads, a diagnosis of the biggest underperformer and why, and two or three specific, data-tied next actions — with the numbers verified against the source, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, performance analysis, marketing metrics (CTR, CPC, CPA, conversion, open/click rate), diagnosing underperformance, data privacy, verification",
 steps=[
 ("Prepare a sample metrics table (use the one below or your own non-confidential sample) and ask AI to read it. Paste the prompt and the data.",
  "Analyse these Neighbourhood Series launch results and tell me the three most important things they show. Data — Instagram: 40,000 impressions, CTR 1.8%, conversion 2.1%. TikTok: 60,000 impressions, CTR 1.2%, conversion 1.0%. Meta ads: spend $600, CPC $0.45, CPA $18, conversion 2.4%. Google ads: spend $400, CPC $0.90, CPA $30, conversion 1.6%. Launch email: sent 2,000, open 26%, click 4.5%, conversion 3.2%. Which channel is most and least efficient?"),
 ("Ask focused diagnostic questions. Paste the prompt below.",
  "From that data: which channel has the best cost per acquisition and which the worst, and why might that be? What is most likely dragging TikTok's conversion despite its reach? Where is ad budget being spent least efficiently? Give me a short, specific answer for each, not a generic summary."),
 ("Get specific, data-tied next actions. Paste the prompt below.",
  "Based only on this data, recommend three specific next actions to improve overall cost per acquisition and conversion in the next two weeks — for example shifting budget, changing a channel's creative or CTA, or pausing something. Tie each recommendation to the number that justifies it."),
 ("Verify before you trust: check AI's reading against the source numbers — does its 'best CPA' match the table, has it invented any figure or trend? Correct anything wrong and note in one line that email and Meta are the efficient channels here.", ""),
 ("Note the data-privacy rule: you used only sample data; you will never paste real customer lists, personally identifiable data or confidential revenue into a public AI tool, and you anonymise or aggregate before any AI analysis.", ""),
 ("Save your verified performance analysis, the diagnosis and the three data-tied next actions in your project folder. These insights feed the report in Lab 15.", ""),
 ],
 test="You have an AI-assisted analysis of the sample metrics with the key reads verified against the source (email and Meta are the efficient channels, Google the least), a specific diagnosis of the biggest issue, and two or three data-tied next actions, plus a noted data-privacy rule — all saved in your project folder.",
 ),
 dict(
 num=14, topic=4,
 title="Automate a Marketing Workflow",
 objective="Use AI to identify a repetitive marketing task and design a practical, repeatable automation for it — with a clear trigger, steps, a human review point and a brand-voice check — that your team could actually run.",
 desc="Much marketing work is repetitive, and that is exactly what AI plus automation can take off your plate. "
 "In this lab you map the repeatable tasks in the Neighbourhood Series workflow (repurposing a blog into social "
 "posts, drafting weekly captions, summarising performance, answering common customer questions) and choose one "
 "to automate. You use a chat assistant to design the automation as a clear blueprint: the trigger that starts "
 "it, the step-by-step flow, the AI prompt at its core, and — crucially — the human review point before "
 "anything publishes and the check that output stays on brand and accurate. You also see how this could be "
 "built with a custom GPT or project, or a no-code tool like Zapier or Make, and you note the guardrails. The "
 "goal is a safe, repeatable workflow, not just speed. " + PROJECT_NOTE,
 build="An automation blueprint for one repetitive marketing task — trigger, step-by-step flow, the core AI prompt, a human review point and a brand-voice/accuracy check — plus a note on how to build it (custom GPT/project or Zapier/Make), saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, custom GPT / project, Zapier / Make, workflow automation, prompt chaining, human-in-the-loop guardrails",
 steps=[
 ("Map the repetitive tasks and pick one. Paste the prompt below.",
  "For a small brand running the Neighbourhood Series campaign, list the marketing tasks that are repetitive enough to automate with AI (for example repurposing content, drafting weekly captions, summarising weekly performance, answering common customer FAQs). Rank them by how much time they save versus how risky they are to automate, and recommend the best first one to automate."),
 ("Design the automation as a blueprint. Paste the prompt below (using the task you chose — here, repurposing a blog post into a week of social content).",
  "Design a step-by-step AI automation for this task: turn one new blog post into a week of on-brand social posts for Instagram and TikTok. Give me: the trigger that starts it, each step in order, the core AI prompt it would use (with slots), where a human must review before anything is scheduled, and how it checks the output is on brand and accurate. Present it as a numbered workflow."),
 ("Add the guardrails. Paste the prompt below.",
  "For that automation, list the guardrails a small brand should put in place so it stays safe: what should never be auto-published without review, how to keep brand voice consistent, how to avoid inaccurate claims, and what customer data must never enter the tool. Keep each to one line."),
 ("Note how to build it: in one line each, describe how you could implement this as (a) a custom GPT or Claude Project with saved instructions and your voice guide, and (b) a no-code automation in Zapier or Make that calls an AI step — and which suits a small brand starting out.", ""),
 ("Review the blueprint: does it have a clear trigger, a human review point before publishing, and a brand/accuracy check? Confirm no step auto-publishes unreviewed content or handles confidential customer data. Tighten any weak guardrail.", ""),
 ("Save your automation blueprint, guardrails and build notes in your project folder. This is the workflow-automation layer of your playbook.", ""),
 ],
 test="You have an automation blueprint for one repetitive marketing task with a clear trigger, ordered steps, the core AI prompt, a human review point before publishing and a brand-voice/accuracy check, plus guardrails and a note on building it as a custom GPT/project or in Zapier/Make — all saved in your project folder.",
 ),
 dict(
 num=15, topic=4,
 title="Reporting and Insights",
 objective="Use AI to turn the campaign data into a clear, one-page stakeholder report — what happened, why, what it means and what you recommend next — in plain language, and save it as a reusable reporting template.",
 desc="A report is a story for a decision-maker, not a data dump. In this lab you use a chat assistant to turn "
 "your Lab 13 analysis into a concise stakeholder report. You give the AI the verified numbers and the "
 "diagnosis and ask it to draft a one-page report with a clear structure: an executive summary, the headline "
 "results, what the numbers mean, and specific recommended next steps — all in plain language a busy manager "
 "can act on. You sharpen it by asking for the single most important insight and the one recommendation you "
 "would lead with, and you apply your own judgement so the recommendation is sound and specific rather than "
 "generic. Finally, you turn the structure into a reusable monthly reporting template with the prompt that "
 "generates it, so future reporting is fast and consistent. " + PROJECT_NOTE,
 build="A one-page Neighbourhood Series stakeholder report — executive summary, headline results, what they mean, and recommended next steps — plus the single lead insight and recommendation, saved as a reusable monthly reporting template with its prompt, in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, reporting, executive summary, turning data into narrative, insights and recommendations, a reusable report template",
 steps=[
 ("Draft the one-page report. Paste the prompt below with your verified analysis from Lab 13.",
  "You are a marketing analyst writing for a busy business owner. Using this verified analysis of the Neighbourhood Series launch [paste your Lab 13 numbers and diagnosis], write a clear one-page report with: (1) a three-sentence executive summary, (2) the headline results by channel, (3) what the numbers mean in plain language, and (4) three specific recommended next steps. Avoid jargon; make it easy to act on."),
 ("Sharpen to the single insight. Paste the prompt below.",
  "From that report, what is the single most important insight, and the one recommendation I should lead with in a meeting? State each in one sentence, and explain in one line why it matters most."),
 ("Pressure-test the recommendations with your judgement. Paste the prompt below.",
  "Review your three recommendations: for each, is it specific, realistic for a small brand, and clearly justified by the data? Rewrite any that is vague or generic into a concrete action with an expected effect. Do not recommend anything the data does not support."),
 ("Apply your own read: adjust the report so the lead insight and recommendation match what you actually saw in Lab 13 (email and Meta efficient, Google least efficient, TikTok reach not converting). Make sure nothing overclaims.", ""),
 ("Turn it into a reusable template. Paste the prompt below.",
  "Turn this report structure into a reusable monthly marketing report template with clearly labelled sections and placeholders for the metrics, and give me the single prompt I can paste each month (with slots for the new data) to generate the report in this format and voice."),
 ("Save your one-page report, the lead insight and recommendation, and the reusable reporting template (with its prompt) in your project folder. This is the reporting layer of your playbook.", ""),
 ],
 test="You have a clear one-page stakeholder report (executive summary, headline results, meaning and three specific, data-justified recommendations), the single lead insight and recommendation, and a reusable monthly reporting template with its prompt — all matching your verified analysis and saved in your project folder.",
 ),
 dict(
 num=16, topic=4,
 title="Build Your AI Marketing Playbook",
 objective="Assemble everything from the course into one reusable AI Marketing Playbook for the Neighbourhood Series and beyond, then structure and rehearse a short presentation of the campaign — the capstone deliverable.",
 desc="This capstone brings the whole course together. You use a chat assistant to assemble every piece you "
 "have built — your AI toolkit and prompt library, the brand voice and personas, the content kit, the keyword "
 "research, the campaign plan, the personalised and tested content, the performance analysis, the automation "
 "blueprint and the reporting template — into one structured AI Marketing Playbook: a reusable reference that "
 "lets you (or a teammate) run the next campaign faster. You have AI help you outline the playbook, write a "
 "short 'how to use this' introduction, and define a simple reporting-and-optimisation cadence. Then you build "
 "and rehearse a short presentation of the Neighbourhood Series campaign — the story, the plan, the content and "
 "the results — using AI to structure the narrative and anticipate questions. You leave with a finished, "
 "reusable playbook and a campaign you can present. " + PROJECT_NOTE,
 build="A complete, structured AI Marketing Playbook assembling every course deliverable (toolkit, prompt library, voice and personas, content kit, research, plan, tested content, analytics, automation, reporting) with a 'how to use this' intro and an optimisation cadence, plus a short rehearsed presentation of the Neighbourhood Series campaign.",
 services="ChatGPT / Claude / Gemini / Copilot, assembling a playbook, knowledge structuring, optimisation cadence, presentation structuring, pitch rehearsal",
 steps=[
 ("Outline the playbook. Paste the prompt below.",
  "You are helping me assemble an AI Marketing Playbook from a full course project. I have: an AI toolkit and prompt library, a brand voice guide and three personas, a multi-channel content kit (social, ads, email, images, video), keyword research, a multi-channel campaign plan, personalised and A/B-tested content, a performance analysis, an automation blueprint and a reporting template. Give me a clear, logical structure (sections and sub-sections) for a reusable playbook that lets me or a teammate run the next campaign faster."),
 ("Write the 'how to use this' introduction and cadence. Paste the prompt below.",
  "Write a short introduction (under 150 words) for my AI Marketing Playbook that explains what it is and how to use it for the next campaign, and propose a simple monthly reporting-and-optimisation cadence (what to review, what to test, what to report) that fits a small brand."),
 ("Assemble the playbook: gather your saved deliverables into the structure from Step 1, drop in the intro and cadence, and confirm each section points to the actual prompt or asset you created. Note any gap to fill later.", ""),
 ("Structure the campaign presentation. Paste the prompt below.",
  "Help me present the Neighbourhood Series campaign in five minutes. Give me a slide-by-slide outline: the brand and the opportunity, the audience and insight, the campaign idea and plan, the content (with the hero visual and video), and the early results and next steps. For each slide, one line on what I say. Keep it on the Kopi Culture Co. voice."),
 ("Rehearse and anticipate questions. Paste the prompt below, then practise the pitch aloud once.",
  "List the five questions a business owner is most likely to ask about this campaign (budget, expected return, why these channels, why AI, what's next) and give me a concise, honest one-line answer to each, grounded in my plan and results."),
 ("Review and finalise: confirm the playbook is complete and reusable, the presentation tells a clear story, and nothing overclaims. Save the finished AI Marketing Playbook and the presentation outline in your project folder — the campaign the course set out to build is done.", ""),
 ],
 test="You have a complete, structured AI Marketing Playbook that assembles every course deliverable with a 'how to use this' intro and an optimisation cadence, plus a five-minute campaign presentation outline and prepared answers to the likely questions — rehearsed once and saved in your project folder.",
 ),
]
