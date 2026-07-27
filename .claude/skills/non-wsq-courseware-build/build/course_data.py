"""
SINGLE SOURCE OF TRUTH — C1468 Generative AI for Digital Marketing (non-WSQ).

A two-day, hands-on course on using generative AI as a digital-marketing partner
— to plan campaigns, research audiences, create content across channels, and
analyse and automate marketing work. Using general chat assistants (ChatGPT,
Claude, Gemini and Microsoft Copilot) and AI image and video tools, learners take
one product launch — the "Neighbourhood Series" launch for a fictional Singapore
specialty-coffee brand, Kopi Culture Co. — from a blank page to a complete,
multi-channel digital-marketing campaign and a reusable AI Marketing Playbook:
setting up an AI marketing toolkit and prompt library, defining a brand voice and
audience personas, creating responsibly, producing social, ad, email, image and
video content, keeping the brand consistent across channels, researching audiences
and keywords, planning a multi-channel campaign, personalising and scaling
content, A/B testing and optimising, analysing performance, automating workflows,
reporting insights, and assembling the whole playbook. Every artifact (PPT, LP,
LG, LG.md) and every lab is generated from this module + data_domainN.py so they
stay 100% aligned.

NON-WSQ RULES — the engine enforces these, do not reintroduce them here:
  * NO assessment of any kind (no WA/SAQ, no PP, no case study, no marking).
  * NO SSG / SkillsFuture / WSQ funding or subsidy content.
  * NO TRAQOM survey, NO digital attendance, NO 75% attendance rule.
  * NO TGS course reference — this course carries the plain code C1468.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "Generative AI for Digital Marketing (C1468)"
SHORT_TITLE  = "Generative AI for Digital Marketing (C1468)"   # used in output filenames
COURSE_CODE  = "C1468"                                          # non-WSQ code — never a TGS- ref
VERSION      = "v1.0"
VERSION_DATE = "27 July 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr. Alfred Ang"
DAYS         = 2
MODE         = "Instructor-led, hands-on practical labs"

DARK_THEME = False

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Explain how generative AI supports digital marketing, and set up an AI marketing toolkit — general chat assistants (ChatGPT, Claude, Gemini, Copilot) and AI image and video tools — for marketing work.",
    "LO2: Write effective, structured marketing prompts and build a reusable marketing prompt library.",
    "LO3: Use generative AI to define a consistent brand voice and to build clear audience personas for a campaign.",
    "LO4: Generate marketing copy, images and ideas with AI, applying responsible-use practices — originality, accuracy of claims, disclosure and platform rules.",
    "LO5: Create platform-appropriate social media content — post concepts, hooks, captions and a content calendar — with AI.",
    "LO6: Write ad and email copy with AI — ad headlines and body variations, and launch and nurture emails with clear calls to action.",
    "LO7: Generate on-brand images and short-form marketing videos with AI image and video tools.",
    "LO8: Maintain brand voice and consistency across channels, and repurpose one core piece of content into many.",
    "LO9: Research audiences and keywords with AI — deepen personas, and build keyword clusters for SEO and paid search.",
    "LO10: Plan a multi-channel marketing campaign with AI — objectives, funnel, channel mix, content map and timeline.",
    "LO11: Personalise and scale marketing content with AI — variants by segment and channel — without losing the brand voice.",
    "LO12: Design and run A/B tests with AI — hypotheses, variants and metrics — and use the results to optimise.",
    "LO13: Analyse marketing performance with AI — read the key metrics, diagnose what is underperforming and decide the next action.",
    "LO14: Automate repetitive marketing workflows with AI — design a practical, repeatable automation for your team.",
    "LO15: Turn marketing data into reporting and insights with AI — a clear performance summary and next-step recommendations.",
    "LO16: Combine everything into a reusable AI Marketing Playbook and present the campaign.",
]
LO_TITLES = [
    "AI marketing toolkit",
    "Marketing prompting",
    "Voice & personas",
    "Responsible generation",
    "Social content",
    "Ad & email copy",
    "Images & video",
    "Brand consistency",
    "Audience & keywords",
    "Campaign plan",
    "Personalise & scale",
    "A/B test & optimise",
    "Performance analysis",
    "Workflow automation",
    "Reporting & insights",
    "Marketing playbook",
]

# ------------------------------------------------------------------ topics
# `concepts` are plain strings ("Title — explanation.") so they render cleanly
# as both slide tiles and Learner-Guide bullets. `weighting` = share of course time.
TOPICS = [
    dict(num=1, code="01",
         title="Getting Started with Generative AI for Marketing",
         subtitle="Introduction to generative AI for digital marketing · Popular GenAI tools (ChatGPT, Claude, image and video generators) · Writing effective prompts for marketing · Generating copy, images and ideas",
         weighting="25%",
         concepts=[
            "Generative AI as a marketing partner — a generative AI assistant is a tireless teammate across the whole marketing workflow: it researches, plans, writes, illustrates, analyses and reports, turning a blank page into a fast first draft that you shape into an on-brand, on-strategy campaign.",
            "Where AI helps in digital marketing — marketing runs on a cycle (understand the audience, plan the campaign, create the content, publish across channels, measure and optimise); AI can accelerate every stage, but the strategy, brand judgement and final decisions stay yours.",
            "Popular GenAI tools — ChatGPT, Claude, Gemini and Microsoft Copilot are general chat assistants that generate and refine text, ideas and analysis; AI image tools (DALL·E in ChatGPT, Adobe Firefly, Microsoft Designer, Gemini, Canva) and AI video tools generate visuals and short clips from a prompt. The prompting skills you learn transfer across all of them.",
            "What AI is good (and not good) at — AI is strong at volume, variation, drafting, summarising and first-pass analysis; it is weak at knowing your brand, your real customers and your live numbers, and it will confidently state things that are wrong, so you brief it well, verify, and decide.",
            "The generate–review–refine loop — every marketing AI task follows the same loop: you prompt, the AI generates options, you review them against the brand and the goal, and you refine with follow-up prompts and your own edits until it is right. This loop drives every lab.",
            "Prompting is the core marketing skill — a strong marketing prompt gives the AI a role, the context (brand, audience, goal, channel), the exact task, the format you want back and clear constraints (tone, length, what to avoid); a vague ask gives generic output, a structured ask gives usable, on-brand marketing content.",
            "A reusable marketing prompt library — the same marketing tasks recur on every campaign (audience research, ad copy, captions, subject lines, image briefs, analysis), so you save your best prompts as reusable templates with clearly marked slots you fill in for any brief.",
            "Brand voice and audience come first — AI only sounds like your brand and speaks to your customer when you tell it who the brand is and who the audience is; you define the voice and the personas early and hold every AI output to them.",
            "Generating copy, images and ideas — from one good brief, AI can produce a batch of campaign ideas, draft copy and starter visuals in minutes; you treat all of it as raw material to curate, fact-check and make genuinely your own.",
            "Responsible and transparent use — you keep confidential customer data and unpublished plans out of public AI tools, check every claim and statistic, respect copyright and the ad platforms' rules, avoid imitating a real brand, and are transparent about AI assistance where it matters.",
         ]),
    dict(num=2, code="02",
         title="Content Creation with Generative AI",
         subtitle="Creating social media content · Writing ad and email copy · Generating images and videos · Maintaining brand voice and consistency",
         weighting="25%",
         concepts=[
            "Content on a defined voice — on a brand voice and personas you have already defined, AI drafts social posts, ad copy, emails, images and video scripts fast; you give it the brief and voice, generate several options, and choose and sharpen the strongest rather than accepting the first.",
            "Social media content — AI helps you produce platform-appropriate content: scroll-stopping hooks, captions, hashtags and post concepts tuned to how each channel (Instagram, TikTok, Facebook, LinkedIn) actually works, organised into a content calendar.",
            "Every draft is a starting point — an AI post, ad or email is a first draft, not a deliverable: you cut the clichés and filler, add the specific, true details only you know, check every claim, and make the words genuinely the brand's before they go live.",
            "Ad copy that converts — AI generates ad headlines, primary text and description variations for Meta and Google, each built around one clear message and call to action; you produce many variants to test rather than betting on a single line.",
            "Email that gets opened and clicked — AI drafts subject lines, preview text, launch emails and nurture sequences with a clear structure (hook, value, proof, call to action); you keep them on voice, honest and easy to act on.",
            "Generating images and video — AI image tools turn a text prompt into on-brand visuals, and AI video tools turn a script into short-form clips for Reels, TikTok and ads; a strong prompt names the subject, style, composition, lighting, palette, mood and aspect ratio, and you iterate to an on-brand result.",
            "Honest, on-brand visuals — AI images and video can invent garbled text, fake logos, wrong products and impossible details, and can drift off-brand; you review every asset, avoid imitating a real brand's or artist's protected look, and keep one consistent style across the set.",
            "Maintaining brand voice and consistency — a campaign works only when every piece across every channel sounds like one brand; you use AI to run a consistency pass — aligning voice, message and key wording — and to catch anything off-brand before it publishes.",
            "Repurposing one idea into many — the efficient way to create is to make one strong core piece and have AI atomise it into a post, an ad, an email, a caption and a video script, each adapted for its channel while carrying the same message.",
            "Content that works together — social, ad, email, image and video content are strongest when made as a set that shares one voice, one look and one message — which is exactly what your Neighbourhood Series content kit becomes.",
         ]),
    dict(num=3, code="03",
         title="Campaign Planning and Optimisation with AI",
         subtitle="Researching audiences and keywords · Planning multi-channel campaigns · Personalising and scaling content · A/B testing and optimisation",
         weighting="25%",
         concepts=[
            "Research before you create — good marketing starts with understanding the audience and the search landscape; AI accelerates audience research and keyword research so your plan is grounded in real customer language and intent, not guesswork.",
            "Researching audiences with AI — you use AI to deepen your personas: their goals, pain points, objections, the channels they use and the words they use, so every message speaks to a real person rather than 'everyone'.",
            "Keyword research with AI — AI helps you generate seed keywords, cluster them by theme and search intent (informational, commercial, transactional), and map them to content for SEO and to ad groups for paid search — you then verify volume and competition in a real tool.",
            "Planning a multi-channel campaign — a campaign is a plan, not a pile of posts; AI helps you set objectives, map content to the funnel (awareness, consideration, conversion, retention), choose the channel mix, and build a realistic timeline and calendar.",
            "The marketing funnel — you match the message to the stage: awareness content earns attention, consideration content builds trust, conversion content drives the sale, and retention content keeps the customer; AI helps you plan content for each stage.",
            "Budget-aware planning — AI helps you favour high-leverage, small-budget moves (organic social, email, SEO, small partnerships) over big-spend media, so the plan is one a real small brand can actually run.",
            "Personalising content — one core message becomes many tailored versions; AI adapts tone, framing, offer and channel for each persona and segment while keeping the message and voice consistent, so each customer gets a relevant message.",
            "Scaling content without losing the voice — AI lets you produce variants at volume — many ad versions, segmented emails, localised captions — quickly; the discipline is holding every variant to the brand voice and quality bar, not just producing more.",
            "A/B testing with AI — you improve by testing: AI helps you form a clear hypothesis, generate the competing variants (subject lines, headlines, creatives, CTAs), and define the single metric that decides the winner, so you learn what actually works.",
            "Optimising with the results — you read the test outcome, keep the winner, and feed the learning back into the next round; AI helps you interpret the result and suggest the next variant, turning marketing into a continuous improvement loop.",
         ]),
    dict(num=4, code="04",
         title="Analytics and Workflow with AI",
         subtitle="Analysing marketing performance with AI · Automating marketing workflows · Reporting and insights · Building your AI marketing playbook",
         weighting="25%",
         concepts=[
            "From activity to results — the point of marketing is outcomes, not output; AI helps you close the loop by reading performance data, explaining what happened, and pointing to the next action, so effort turns into learning.",
            "Analysing performance with AI — you paste campaign metrics (impressions, click-through rate, cost per click, cost per acquisition, conversion rate, email opens and clicks, engagement) and AI helps you spot the story in the numbers, flag underperformers and surface what to do next — you keep judgement over the final call.",
            "Ask the right questions of your data — AI analysis is only as good as your question; you learn to ask focused questions ('which channel has the best cost per acquisition and why', 'what is dragging conversion') so the answer is actionable, not a generic summary.",
            "Verify before you act — AI can misread a table or invent a trend, so you sanity-check its numbers against the source, never paste confidential or personally identifiable customer data into a public tool, and treat its analysis as a fast first read you confirm.",
            "Automating marketing workflows — much marketing work is repetitive (repurposing content, drafting variants, summarising reports, answering FAQs); AI plus automation tools (a custom GPT or project, Zapier, Make, Copilot) can turn a repeated task into a reliable, repeatable workflow.",
            "Designing a safe automation — a good automation has a clear trigger, defined steps, a human review point before anything publishes, and a check on quality and brand voice; you design the guardrails, not just the speed.",
            "Reporting and insights — a report is not a data dump; AI helps you turn the numbers into a short, clear story for stakeholders — what happened, why, what it means, and what you recommend next — in plain language.",
            "Insight, not just numbers — the value of a report is the insight and the recommendation; you use AI to draft the narrative and the next steps, then apply your judgement so the recommendation is sound and specific.",
            "Building your AI marketing playbook — the lasting output is a reusable playbook: your tools, prompt library, brand voice and personas, channel playbooks, campaign plan, automations and reporting cadence, assembled so you (and your team) can run the next campaign faster.",
            "You are the marketer — across every technique, AI generates, drafts and analyses, but you set the strategy, judge the options, protect the brand and the customer's trust, and make the final call; the tools amplify your marketing, they do not replace it.",
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Set the foundation and create the content — set up an AI marketing toolkit, define the Kopi Culture Co. brand voice and audience personas, learn responsible generation, then produce the Neighbourhood Series social, ad, email, image and video content on one consistent brand voice.",
    2: "Plan, optimise, analyse and automate — research audiences and keywords, plan the multi-channel campaign, personalise and scale the content, A/B test and optimise, analyse performance, automate the workflow, report the insights, and assemble the reusable AI Marketing Playbook.",
}

# ------------------------------------------------------------------ schedule
# NON-WSQ: no assessment blocks. Each day totals exactly 480 scheduled minutes
# (excluding the 1-hour lunch); the 30 minutes of tea breaks sit inside that, so
# the instructional total is 7.5 hours per day (15 hours across the two days).
def SCHEDULE(lab_titles):
    return {
     1: (DAY_THEMES[1], [
        ("9:00","9:20",20,"admin","Welcome, course introduction, ground rules, and setup: signing in to ChatGPT, Claude, Gemini and Microsoft Copilot and to an AI image and video tool, and confirming each tool is ready for the labs"),
        ("9:20","10:00",40,"topic","TOPIC 01 — Getting Started with Generative AI for Marketing: introduction to generative AI for digital marketing; popular GenAI tools (ChatGPT, Claude, image and video generators); writing effective prompts for marketing; generating copy, images and ideas (concepts + live demo)"),
        ("10:00","10:45",45,"lab","Hands-on: "+lab_titles([1])),
        ("10:45","11:00",15,"break","Tea break"),
        ("11:00","13:00",120,"lab","Hands-on: "+lab_titles([2,3,4])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:30",30,"topic","TOPIC 02 — Content Creation with Generative AI: creating social media content; writing ad and email copy; generating images and videos; maintaining brand voice and consistency (concepts + live demo)"),
        ("14:30","16:00",90,"lab","Hands-on: "+lab_titles([5,6])),
        ("16:00","16:15",15,"break","Tea break"),
        ("16:15","17:50",95,"lab","Hands-on: "+lab_titles([7,8])),
        ("17:50","18:00",10,"recap","Day 1 recap: the brand voice, personas and the Neighbourhood Series content kit built so far, and a look ahead to campaign planning and analytics on Day 2"),
     ]),
     2: (DAY_THEMES[2], [
        ("9:00","9:10",10,"admin","Day 1 recap and Day 2 overview: from the content kit to a planned, optimised, measured and automated campaign"),
        ("9:10","9:45",35,"topic","TOPIC 03 — Campaign Planning and Optimisation with AI: researching audiences and keywords; planning multi-channel campaigns; personalising and scaling content; A/B testing and optimisation (concepts + live demo)"),
        ("9:45","10:45",60,"lab","Hands-on: "+lab_titles([9,10])),
        ("10:45","11:00",15,"break","Tea break"),
        ("11:00","13:00",120,"lab","Hands-on: "+lab_titles([11,12])),
        ("13:00","14:00",60,"lunch","Lunch break"),
        ("14:00","14:30",30,"topic","TOPIC 04 — Analytics and Workflow with AI: analysing marketing performance with AI; automating marketing workflows; reporting and insights; building your AI marketing playbook (concepts + live demo)"),
        ("14:30","16:00",90,"lab","Hands-on: "+lab_titles([13,14])),
        ("16:00","16:15",15,"break","Tea break"),
        ("16:15","17:45",90,"lab","Hands-on: "+lab_titles([15,16])),
        ("17:45","18:00",15,"recap","Course wrap-up: presenting the Neighbourhood Series campaign and the AI Marketing Playbook, responsible-AI and data-privacy recap, and next steps"),
     ]),
    }

# ------------------------------------------------------------------ deck content
COURSE_OVERVIEW = dict(
    section_title="Course Fundamentals",
    concepts_title="What Generative AI for Digital Marketing Really Is",
    concepts=[
        "A partner for the whole marketing workflow — you describe a marketing task in words and AI returns usable first drafts (audience research, a campaign plan, copy, images, video scripts, analysis) in seconds, which you then curate, refine and make on-brand.",
        "Two toolsets, one campaign — chat assistants (ChatGPT, Claude, Gemini, Copilot) generate the ideas, words, plans and analysis; AI image and video tools generate the visuals. You learn to move marketing work smoothly between them.",
        "Generate, review, decide — the workflow is always the same: give a structured prompt, review the options against the brand and the goal, and take ownership of the result. The AI generates; you set the strategy and decide.",
        "Results are the point — the aim is not just making content faster; it is running a better campaign — better targeted, more consistent, tested and measured — while the strategy, brand and the customer's trust stay yours.",
    ],
    framework_title="The AI-Assisted Marketing Workflow",
    framework=[
        ("Understand", "Use AI to research the audience and the keywords, and to define the brand voice and personas — so every output is judged against a real customer and a real goal."),
        ("Plan", "Use AI to set objectives, map content to the funnel, choose the channel mix, and build a realistic, budget-aware campaign plan and calendar."),
        ("Create", "Draft the social, ad, email, image and video content — all on one voice and one look — and repurpose one core idea across every channel."),
        ("Optimise", "Personalise and scale the content by segment, then A/B test the key elements and keep the winners — improving with each round."),
        ("Measure", "Analyse the performance, report the insights and recommendations in plain language, automate the repetitive work, and capture it all in a reusable playbook."),
    ],
    statement=dict(
        headline="Generative AI gives you a fast first draft of every part of a marketing campaign — the craft is prompting well, planning with strategy, curating with brand judgement, testing what works, and directing the campaign yourself.",
        body="This course is hands-on: you take one product launch — the Neighbourhood Series for Kopi Culture Co., a fictional Singapore specialty-coffee brand releasing a range of local-flavour drip-bag coffees and a monthly subscription — from a blank page to a complete, multi-channel digital-marketing campaign and a reusable AI Marketing Playbook, using ChatGPT, Claude, Gemini, Microsoft Copilot and AI image and video tools.",
        kicker="THE MARKETING RULE",
    ),
    pillars_title="What You'll Build",
    pillars=[
        ("An AI marketing toolkit", ["ChatGPT, Claude, Gemini, Copilot and image/video tools set up", "A reusable marketing prompt library", "A locked brand voice and audience personas"]),
        ("A multi-channel content kit", ["Social posts, hooks, captions and a calendar", "Ad copy and launch and nurture emails", "On-brand images and short-form video"]),
        ("A planned, optimised campaign", ["Audience and keyword research", "A multi-channel campaign plan and funnel", "Personalised, scaled and A/B-tested content"]),
        ("Analytics, automation and a playbook", ["An AI performance analysis and report", "A marketing workflow automation blueprint", "A reusable AI Marketing Playbook"]),
    ],
    arc_title="How Every Lab Works",
    arc=[
        "The trainer demonstrates the AI technique on the shared Kopi Culture Co. Neighbourhood Series campaign example.",
        "You run it yourself in ChatGPT, Claude, Gemini, Copilot or your AI image/video tool using the supplied Kopi Culture Co. brief.",
        "You verify the result against the lab's explicit 'Test it' check.",
        "You review and refine — curate the options, cut the clichés, check the claims, fix anything off-brand — until it meets the standard.",
        "You keep the reviewed output — each becomes the next part of your Neighbourhood Series campaign and AI Marketing Playbook.",
    ],
)

# ------------------------------------------------------------------ LG content
LG_INTRO = (
    "This Learner Guide accompanies the Generative AI for Digital Marketing (C1468) course, conducted by "
    "Tertiary Infotech Academy Pte Ltd. It carries the full detail of all 16 hands-on labs, in the order you "
    "will run them across the two days, together with the concepts each lab depends on."
)
LG_INTRO2 = (
    "The labs build a single, connected deliverable — the Neighbourhood Series launch campaign, a multi-channel "
    "digital-marketing campaign for Kopi Culture Co., a fictional Singapore specialty-coffee brand releasing a "
    "range of local-flavour drip-bag coffees and a monthly subscription. You start in Lab 1 by setting up "
    "ChatGPT, Claude, Gemini, Microsoft Copilot and AI image and video tools as a marketing toolkit, then in "
    "every lab you take the campaign one stage further — a reusable marketing prompt library, a locked brand "
    "voice and audience personas, responsible-generation ground rules, social, ad, email, image and video "
    "content, a brand-consistency pass, audience and keyword research, a multi-channel campaign plan, "
    "personalised and scaled content, A/B tests, a performance analysis, an automation blueprint, a stakeholder "
    "report, and finally a reusable AI Marketing Playbook. A Kopi Culture Co. brief with the brand facts you "
    "need is supplied in labs/reference-pack/; you may substitute your own non-confidential brand or product "
    "wherever you prefer."
)
LG_SETUP = dict(
    needs=[
        "A laptop (Windows or Mac) with a modern web browser (Chrome, Edge, Safari or Firefox) and a reliable internet connection — every generative feature runs in the cloud.",
        "Access to at least one general chat assistant — ChatGPT (chat.openai.com), Claude (claude.ai), Gemini (gemini.google.com) or Microsoft Copilot (copilot.microsoft.com); a free account for each is enough to follow the labs, and the trainer will confirm what is available.",
        "Access to one AI image tool — the image feature in ChatGPT (DALL·E), Gemini, Microsoft Copilot / Designer, Adobe Firefly (firefly.adobe.com) or Canva (canva.com) — and, for the video lab, access to an AI video feature (for example in Canva, Gemini/Veo, or a free text-to-video tool the trainer indicates). A free option is enough.",
        "A signed-in account for each tool you will use, tested before Lab 1 with a simple 'hello' prompt so you know it responds, plus somewhere to keep your work (a documents folder or notes app).",
        "The supplied Kopi Culture Co. brief and fact sheet (brand story, the Neighbourhood Series range, audiences, channels and voice notes) in labs/reference-pack/ — or a few notes and non-confidential facts from your own brand or product to use instead.",
    ],
    verify_text="Before Lab 1, confirm you can sign in to at least one chat assistant and to an AI image tool, send a simple prompt and get a reply, and that you have the Kopi Culture Co. brief to hand. If anything is missing, tell the trainer.",
    verify_code="Open chat.openai.com (ChatGPT) · claude.ai (Claude) · gemini.google.com (Gemini) · copilot.microsoft.com (Copilot)  ·  sign in  ·  send \"Hello, are you ready to help me plan a digital marketing campaign?\"  ·  confirm a reply",
    conventions=[
        "Placeholders such as <YOUR BRAND>, <YOUR AUDIENCE> or <PASTE METRICS> are replaced with your own values before you send a prompt.",
        "Prompts to paste into ChatGPT, Claude, Gemini, Copilot or your AI image/video tool are shown in the 'Prompt to use' blocks — adapt the bracketed parts to your own project.",
        "Where a lab says 'any assistant', use whichever chat tool you prefer; the image and video steps use any AI image/video tool you have access to.",
        "Every lab ends with a 'Test it' step — an explicit check that the reviewed output meets the standard before you move on.",
        "Keep every reviewed output and prompt in one project folder (KCC-Neighbourhood-Series) so your campaign and its material stay together and consistent.",
    ],
)
LAB_NOTE = (
    "Use only brands, data and material you are authorised to use. Do not paste confidential customer data, "
    "personal information, credentials or unpublished plans into a public AI tool. Use the supplied Kopi Culture "
    "Co. brief rather than real client material, treat every AI output — copy, images, video and especially any "
    "statistic or performance analysis — as a first draft to be reviewed, fact-checked and made on-brand, avoid "
    "imitating a real brand's protected identity, follow each ad platform's rules, and be transparent about AI "
    "assistance where appropriate before anything goes to a real audience."
)
LG_WRAPUP = dict(
    title="Wrap-Up",
    intro="You have taken one product launch — the Neighbourhood Series for Kopi Culture Co. — from a blank page to a complete, multi-channel digital-marketing campaign and a reusable AI Marketing Playbook across two days, using ChatGPT, Claude, Gemini, Microsoft Copilot and AI image and video tools as marketing partners while keeping the strategy, the brand voice, the accuracy and the final decisions your own.",
    sections=[
        dict(title="What you built", bullets=[
            "An AI marketing toolkit — ChatGPT, Claude, Gemini, Copilot and AI image and video tools set up, plus a reusable marketing prompt library, a locked brand voice and clear audience personas.",
            "A multi-channel content kit — social posts, hooks, captions and a calendar; ad and email copy; on-brand images and short-form video — all on one voice and made responsibly.",
            "A planned, optimised campaign — audience and keyword research, a multi-channel campaign plan and funnel, personalised and scaled content, and A/B tests with the winners kept.",
            "Analytics, automation and a playbook — an AI performance analysis, a stakeholder report with recommendations, a workflow-automation blueprint, and a reusable AI Marketing Playbook.",
            "One connected campaign that carries the whole launch — plan, content, optimisation, analytics and playbook — ready to run and to reuse.",
        ]),
        dict(title="What to do next", bullets=[
            "Rebuild a campaign for a real, non-confidential brand or product of your own using the same workflow, prompt library and playbook.",
            "Introduce your saved prompts, brand-voice guide and personas to your team so everyone markets on the same voice and to the same customer.",
            "Always start with the audience, the brand and the goal before you generate — AI makes creating and analysing faster, it does not supply your strategy or your judgement.",
            "Keep the responsible habit: protect customer data, verify every claim and number, respect copyright and platform rules, and be transparent about AI assistance.",
        ]),
    ],
)
LG_NEXT_STEPS = [
    "First pass: complete every lab yourself, following the steps and verifying each 'Test it' check.",
    "Second pass: rebuild the campaign for your own real, non-confidential brand or product, from voice and personas to a reported, optimised campaign.",
    "Introduce your prompt library and the understand → plan → create → optimise → measure workflow to your team so the practice sticks.",
    "Review each lab's detailed steps in this guide and re-create the campaign in your own AI tools.",
]
LG_GLOSSARY = [
    ("Generative AI assistant", "A general-purpose chat tool (ChatGPT, Claude, Gemini, Microsoft Copilot) that generates text, ideas and analysis from a prompt."),
    ("AI image tool", "A tool that generates images from a text prompt — DALL·E in ChatGPT, Adobe Firefly, Microsoft Designer, Gemini or Canva."),
    ("AI video tool", "A tool that generates or assembles short video from a prompt or script — for example Canva, Gemini/Veo, or a text-to-video generator."),
    ("Prompt", "The instruction you give the AI; a structured prompt with role, context, task, format and constraints produces a far better result than a vague one."),
    ("Prompt library", "A saved, reusable set of prompt templates for the recurring marketing tasks — research, copy, captions, subject lines, image briefs, analysis."),
    ("Generate–review–refine loop", "The core marketing AI workflow — prompt, review the options against the brand and goal, then refine with follow-up prompts and your own edits."),
    ("Brand voice", "The consistent personality and tone of a brand that makes its content recognisably its own, across every channel."),
    ("Audience persona", "A short, concrete profile of a target customer — goals, pain points, channels and language — that every message is written for."),
    ("Marketing funnel", "The customer journey from awareness to consideration to conversion to retention; content is matched to each stage."),
    ("Multi-channel campaign", "A coordinated campaign that runs across several channels (social, search, email, web) with one message and goal."),
    ("Organic vs paid", "Organic reach is unpaid (posts, SEO, email to your list); paid reach is advertising (Meta and Google ads) you pay to show."),
    ("Social media content", "Platform-appropriate posts — hooks, captions, hashtags, formats — made for how each channel (Instagram, TikTok, Facebook, LinkedIn) works."),
    ("Ad copy", "The headline, primary text and description of an advertisement, built around one clear message and call to action."),
    ("Call to action (CTA)", "The specific action you ask the reader to take — 'Shop the launch', 'Subscribe', 'Learn more'."),
    ("Email marketing", "Reaching your subscribers by email — launch emails, newsletters and nurture sequences — with subject lines, preview text and clear CTAs."),
    ("Subject line / preview text", "The two lines that decide whether an email is opened; short, specific and honest versions win."),
    ("Image prompt", "A text description for an AI image tool that names the subject, style, composition, lighting, palette, mood and aspect ratio."),
    ("Aspect ratio", "The width-to-height shape of an image or video (for example 1:1 for a square post, 9:16 for a story or Reel, 16:9 for a banner)."),
    ("Brand consistency", "Keeping voice, look, message and key wording aligned across every piece of content and every channel."),
    ("Content repurposing", "Turning one core piece of content into many channel-specific pieces (post, ad, email, caption, video) that share the same message."),
    ("Content calendar", "A schedule of what content publishes, on which channel, and when, across a campaign."),
    ("Audience research", "Deepening your understanding of a target customer — goals, pain points, objections, channels and language — to sharpen targeting and messaging."),
    ("Keyword research", "Finding the words and phrases people search for, clustered by theme and intent, to guide SEO content and paid search."),
    ("Search intent", "What a searcher is trying to do — informational, commercial or transactional — which decides the content or ad you serve."),
    ("SEO", "Search Engine Optimisation — earning unpaid search visibility by matching useful content to what people search for."),
    ("Personalisation", "Tailoring the message, offer or framing to a specific persona or segment so it feels relevant to that customer."),
    ("Segmentation", "Dividing an audience into groups (by persona, behaviour or stage) so each group gets a more relevant message."),
    ("A/B test", "A controlled comparison of two versions (A and B) that differ in one element, to see which performs better on a chosen metric."),
    ("Hypothesis", "A clear, testable statement of what you expect to improve and why, that an A/B test is designed to prove or disprove."),
    ("Conversion rate", "The share of people who take the desired action (buy, sign up) out of everyone who had the chance."),
    ("Click-through rate (CTR)", "The share of people who clicked out of those who saw the ad, email or post."),
    ("Cost per click (CPC) / cost per acquisition (CPA)", "What you pay for each click (CPC) or each customer acquired (CPA) — key efficiency metrics for paid marketing."),
    ("Impressions / reach / engagement", "Impressions are times content was shown; reach is unique people who saw it; engagement is the likes, comments, shares and saves it earned."),
    ("Return on ad spend (ROAS)", "Revenue earned for every dollar of advertising spent — a headline measure of paid-campaign efficiency."),
    ("Marketing automation", "Using tools (a custom GPT or project, Zapier, Make, Copilot) to run a repeated marketing task reliably with minimal manual effort."),
    ("Human-in-the-loop", "Keeping a person responsible for reviewing, correcting and approving every AI output before it is published or acted on."),
    ("Hallucination", "A confident but false or invented statement, statistic or trend from an AI, which is why every output and analysis must be verified."),
    ("Responsible AI use", "Using AI safely and ethically — protecting customer and confidential data, verifying claims, respecting copyright and platform rules, and being transparent about AI assistance."),
    ("AI Marketing Playbook", "A reusable reference — tools, prompt library, voice and personas, channel playbooks, campaign plan, automations and reporting cadence — that lets you run the next campaign faster."),
]

# ------------------------------------------------------------------ version history
VERSION_HISTORY = [
    ("1.0", VERSION_DATE, "Initial release — C1468 Generative AI for Digital Marketing courseware.", TRAINER),
]
