# -*- coding: utf-8 -*-
"""
Domain 1 — Getting Started with Generative AI for Marketing. Labs 1-4 (Day 1).

THE CONNECTED PROJECT STARTS HERE, IN LAB 1.

Every lab in this course takes one connected deliverable — the Neighbourhood
Series launch campaign for Kopi Culture Co., a fictional Singapore
specialty-coffee brand — one stage further. Lab 1 sets up the AI marketing
toolkit; Lab 2 builds a reusable marketing prompt library; Lab 3 defines the
brand voice and the audience personas; Lab 4 generates the first copy, images and
ideas responsibly and sets the responsible-generation ground rules for the whole
campaign. A Kopi Culture Co. brief with the brand facts you need is supplied; use
your own non-confidential brand or product instead wherever you prefer.
"""

SCENARIO = (
 "Kopi Culture Co. (KCC) is a fictional Singapore specialty-coffee brand — small-batch roasts and drip-bag "
 "coffee inspired by the city's neighbourhoods and local flavours. After four years building a loyal following "
 "through a small online store and weekend markets, it is launching the Neighbourhood Series: a range of four "
 "local-flavour drip-bag coffees — Tiong Bahru Gula Melaka, Katong Kaya, Geylang Teh Tarik and Toa Payoh Pandan "
 "— plus a monthly subscription, The KCC Club. The launch is timed for the year-end gifting season and aims to "
 "grow online sales and subscriptions. You are the marketer preparing the launch — the Neighbourhood Series "
 "campaign — which must reach new customers and convert them across channels: social posts, ads, email, images "
 "and video, a multi-channel plan, personalised and tested content, performance analysis, an automation, and a "
 "reusable playbook. Across this course you take that campaign from a blank page to a complete, measured "
 "multi-channel campaign using ChatGPT, Claude, Gemini, Microsoft Copilot and AI image and video tools. Use "
 "this scenario only if you cannot use a real, non-confidential brand or product of your own; your own brief is "
 "always welcome."
)

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Neighbourhood Series campaign and AI "
 "Marketing Playbook, the connected campaign you assemble across all 16 labs."
)

DOMAIN1 = [
 dict(
 num=1, topic=1,
 title="Set Up Your AI Marketing Toolkit",
 objective="Sign in to ChatGPT, Claude, Gemini, Microsoft Copilot and an AI image and video tool, run your first marketing prompts, and learn the generate–review–refine loop and where AI helps across the marketing workflow — the foundation every later lab uses.",
 desc="This lab gets you comfortable with the tools before any real marketing work begins. You open the chat "
 "assistants (ChatGPT, Claude, Gemini and Microsoft Copilot), confirm you are signed in, and run a simple "
 "marketing prompt so you see how each generates ideas and copy, then run the same prompt in a second assistant "
 "to feel how they differ. You open an AI image tool, sign in, and generate a quick throwaway product image "
 "from a one-line prompt so you can see what image generation does, and note where an AI video tool fits. You "
 "map where AI genuinely helps across the marketing workflow (research, planning, content, publishing, "
 "measuring) and where it needs you (strategy, brand knowledge, real numbers, judgement). By the end you "
 "understand the generate -> review -> refine loop that is the heart of every lab. " + PROJECT_NOTE,
 build="Your AI marketing toolkit set up and tested — at least one chat assistant and one AI image tool signed in and responding — a first throwaway AI-generated idea list and product image, and a clear, written map of where AI helps across the marketing workflow and the generate–review–refine loop.",
 services="ChatGPT, Claude, Gemini, Microsoft Copilot, an AI image tool, an AI video tool, account sign-in, first marketing prompts, comparing assistants, the generate–review–refine loop",
 steps=[
 ("Create a project folder on your machine called 'KCC-Neighbourhood-Series' so every file and note you make across the two days stays together. Open ChatGPT (chat.openai.com), Claude (claude.ai), Gemini (gemini.google.com) and Microsoft Copilot (copilot.microsoft.com) in browser tabs and confirm you are signed in to at least one.", ""),
 ("In one chat assistant, run a simple first marketing prompt to see how it generates ideas. Paste the prompt below and read the reply.",
  "You are a digital marketing strategist. Give me eight short campaign ideas to launch a range of local-flavour drip-bag coffees for a small Singapore specialty-coffee brand aimed at young urban coffee lovers. Keep each idea to one line."),
 ("Run the exact same prompt in a second assistant and compare the two replies. Notice differences in tone, ideas and range — the skill you learn transfers across all of them, so use whichever you prefer for a given task.",
  "You are a digital marketing strategist. Give me eight short campaign ideas to launch a range of local-flavour drip-bag coffees for a small Singapore specialty-coffee brand aimed at young urban coffee lovers. Keep each idea to one line."),
 ("Open your AI image tool (DALL·E in ChatGPT, Gemini, Microsoft Copilot / Designer, Adobe Firefly or Canva), sign in, and generate a quick throwaway product image from a one-line prompt so you can see what image generation produces. Paste the prompt below.",
  "A premium drip-bag coffee sachet on a marble café table with a cup of black coffee and soft morning light, minimal and modern, product photography, square format."),
 ("Look at what the image tool produced — a generated visual from a text description, in seconds. Note that it is a fast starting point, not a finished asset, and that AI images can invent odd details or garbled text. You will not keep this one; it is only to feel the tool. Note where an AI video tool (Canva, Gemini/Veo or a text-to-video generator) would fit for a Reel or TikTok later.", ""),
 ("Map where AI helps across the marketing workflow. In one line each, note how AI could help at research, planning, content creation, publishing and measuring — and where it needs you (it does not know the Kopi Culture Co. brand, your real customers, or your live numbers). This good/not-good picture guides how you use AI all day.", ""),
 ("Open the supplied Kopi Culture Co. brief (labs/reference-pack/): the brand story, the Neighbourhood Series range and its four coffees, the audiences, the channels and the brand voice notes. Skim it so you know the campaign you are about to build.", ""),
 ("Save your notes into your KCC-Neighbourhood-Series folder. Write one line, in your own words, describing the generate -> review -> refine loop — you rely on it in every later lab.", ""),
 ],
 test="You have signed in to at least one chat assistant and to an AI image tool, run the same prompt in two assistants and compared them, generated a throwaway product image, written a one-line map of where AI helps across the marketing workflow and what it is not good at, skimmed the Kopi Culture Co. brief, and described the generate–review–refine loop in your own words — all saved in your KCC-Neighbourhood-Series folder.",
 ),
 dict(
 num=2, topic=1,
 title="Write Effective Marketing Prompts and Build a Prompt Library",
 objective="Turn a vague marketing ask into a strong, structured prompt (role, context, task, format, constraints), and save a reusable marketing prompt library for the work you repeat on every campaign.",
 desc="A good marketing result starts with a good prompt, not a lucky one. In this lab you read the Kopi "
 "Culture Co. brief and write a deliberately vague prompt first, so you see how generic the result is. You then "
 "rebuild it with five clear parts — a role for the AI, the context (brand, audience, goal, channel), the exact "
 "task, the format you want back, and clear constraints (tone, length, what to avoid) — and watch the output "
 "become genuinely usable and on-brand. You run small single-change edits to feel how each part matters, then "
 "save your best versions as a reusable marketing prompt library with clearly marked slots, covering the tasks "
 "you repeat on every campaign: audience research, ad copy, social captions, email subject lines, image briefs "
 "and performance analysis. " + PROJECT_NOTE,
 build="A structured marketing prompt built from role, context, task, format and constraints, plus a reusable marketing prompt library with clearly marked slots for the recurring marketing tasks, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, the structured prompt framework (role, context, task, format, constraints), prompt iteration, a reusable marketing prompt library",
 steps=[
 ("Open the Kopi Culture Co. brief and note two things you will reuse in every prompt: who the audience is (young urban coffee lovers, busy work-from-home professionals, gift shoppers) and the goal (launch the Neighbourhood Series and grow online sales and subscriptions).", ""),
 ("Write a deliberately vague first prompt in any assistant and generate, so you can see the generic result. Paste the prompt below and read how unfocused and clichéd the reply is.",
  "Write some marketing copy for coffee."),
 ("Rebuild the prompt with a role and the context, and regenerate. Paste the prompt below and compare it with the vague version.",
  "You are a senior copywriter for consumer lifestyle brands. Context: Kopi Culture Co. is a Singapore specialty-coffee brand launching the Neighbourhood Series, a range of four local-flavour drip-bag coffees for the year-end gifting season, aimed at young urban coffee lovers and gift shoppers. Draft a short introduction to the range."),
 ("Now add the exact task, the format you want back, and clear constraints, and regenerate. Paste the prompt below.",
  "As the same copywriter, write three options for a 40-word introduction to the Neighbourhood Series. Make it warm, characterful and proudly local; avoid clichés like 'elevate your mornings' and 'the perfect gift'; do not invent awards, origins or claims. Present them as a numbered list."),
 ("Put the vague result and the structured result side by side. Note in one line how much more usable and on-brand the structured prompt was — this is the core lesson of the day.", ""),
 ("Run two or three single-change edits to feel how each part steers the result — for example change the audience to 'busy work-from-home professionals', or change the tone to 'playful and witty' — and note which you would keep for the Neighbourhood Series.", ""),
 ("Save a reusable marketing prompt library in your project folder: templates for audience research, ad copy, social captions, email subject lines, image briefs and performance analysis, each with clearly marked slots — [ROLE], [CONTEXT], [AUDIENCE], [CHANNEL], [TASK], [FORMAT], [CONSTRAINTS] — that you fill in for any future campaign.", ""),
 ],
 test="You have compared a vague prompt with a structured one built from role, context, task, format and constraints, seen how much better and more on-brand the structured prompt performs, run single-change edits to feel each part, and saved a reusable marketing prompt library with marked slots for the recurring marketing tasks in your project folder.",
 ),
 dict(
 num=3, topic=1,
 title="Define Your Brand Voice and Audience Personas",
 objective="Use AI to define a clear Kopi Culture Co. brand voice and to build the three audience personas from the brief — the foundation every later lab's content and targeting is held to — so the whole campaign sounds like one brand and speaks to real customers.",
 desc="A campaign only works when it sounds like one brand and speaks to a real person. In this lab you use a "
 "chat assistant to articulate the Kopi Culture Co. voice from the brief — the tone (the mood: warm, "
 "characterful, proudly local, a little witty), the style (short, vivid, conversational) and the voice (the "
 "consistent personality) — and to generate voice attributes with side-by-side on-voice and off-voice example "
 "lines plus a short 'words we use / words we avoid' list. You then build the three audience personas — young "
 "urban coffee lovers, busy work-from-home professionals and gift shoppers — each with goals, pain points, the "
 "channels they use and the words they use. You test the voice by rewriting a flat line in it, and refine until "
 "it genuinely sounds like the brand. This voice guide and these personas govern every message you generate for "
 "the rest of the course. " + PROJECT_NOTE,
 build="A Kopi Culture Co. brand voice guide — three to five voice attributes, on-voice vs off-voice example lines, and a 'words we use / words we avoid' list — plus three audience personas with goals, pain points, channels and language, tested by rewriting a flat line in the voice, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, defining brand voice (tone, style, voice), on-voice vs off-voice examples, building audience personas, targeting language",
 steps=[
 ("Open the Kopi Culture Co. brief and read the brand story and voice notes — the brand is small-batch, proudly Singaporean, celebrates neighbourhood culture, is warm and a little witty, and knows its coffee. These are the raw material for the voice.", ""),
 ("Ask AI to articulate the voice from the brief. Paste the prompt below.",
  "You are a brand voice strategist. Based on this brand — Kopi Culture Co., a Singapore specialty-coffee brand: small-batch, proudly local, celebrating the city's neighbourhoods and flavours, warm, characterful and a little witty, and genuinely knowledgeable about coffee — define its brand voice. Give me: (1) three to five voice attributes, each with a one-line description; (2) the tone and the writing style; (3) the kind of personality it should feel like. Keep it concise."),
 ("Make the voice guide usable with concrete examples. Paste the prompt below.",
  "For that Kopi Culture Co. voice, write three short example lines that are ON voice and, next to each, a version that is OFF voice (too generic, too corporate or too hype), and one line explaining the difference. Then give me a short 'words and phrases we use' and 'words and phrases we avoid' list."),
 ("Now build the audience personas. Paste the prompt below and read the three profiles.",
  "Build three concise audience personas for the Neighbourhood Series launch: (1) young urban coffee lovers (25-38) who care about quality, origin and aesthetics and discover brands on Instagram and TikTok; (2) busy work-from-home professionals (30-45) who want great coffee at home with convenience and value a subscription; (3) gift shoppers buying a thoughtful local present in the year-end season. For each persona give: a one-line summary, their goals, their pain points, the channels they use, and three words or phrases they actually use about coffee."),
 ("Test the voice on a real line. Paste the prompt below and judge whether the rewrite truly sounds like the brand.",
  "Here is a flat product line: 'Our new coffee is great and makes a good gift.' Rewrite it in three ways that fully match the Kopi Culture Co. voice you defined, keeping each under 25 words."),
 ("Judge and refine: if a rewrite or a persona still sounds generic, tell the AI exactly what is wrong ('too corporate', 'not local enough', 'personas feel interchangeable') and regenerate until they land. Tighten your voice attributes and personas based on what you learn.", ""),
 ("Save the final brand voice guide — attributes, on-voice/off-voice examples, and the words-we-use/avoid list — and the three personas in your project folder. Every later lab holds its content and targeting to these.", ""),
 ],
 test="You have a brand voice guide with three to five voice attributes, side-by-side on-voice and off-voice example lines and a words-we-use/avoid list, plus three distinct audience personas with goals, pain points, channels and language — tested by rewriting a flat line so it genuinely sounds like Kopi Culture Co. — saved in your project folder.",
 ),
 dict(
 num=4, topic=1,
 title="Generate Your First Copy, Images and Ideas — Responsibly",
 objective="Generate a first batch of marketing copy, a starter image and campaign ideas for the Neighbourhood Series on your defined voice, and set the responsible-generation ground rules — accuracy of claims, originality, disclosure, data privacy and platform rules — that govern every later deliverable.",
 desc="Now you generate real marketing material for the first time, and agree how you will generate it "
 "responsibly. Using your Lab 3 voice and personas, you prompt AI for a batch of Neighbourhood Series campaign "
 "ideas, a short copy draft and a starter product image, so you see the whole generate–review–refine loop on "
 "actual deliverables. Then you build a practical responsible-use checklist for AI-assisted marketing and apply "
 "it: you probe where AI marketing goes wrong — inventing statistics, awards or ingredients; making claims you "
 "can't back up; echoing a real competitor's identity; pasting confidential customer data into a public tool; "
 "breaking an ad platform's rules; or hiding AI assistance where it matters — and you decide the brand's "
 "position on each. By the end you have your first content and the ground rules that keep every later lab's "
 "output accurate, original and safe to publish. " + PROJECT_NOTE,
 build="A first batch of Neighbourhood Series campaign ideas, a short on-voice copy draft and a starter product image, plus a responsible-generation checklist applied to the campaign — covering accuracy of claims, originality, disclosure, customer-data privacy and ad-platform rules — with the brand's decisions recorded.",
 services="ChatGPT / Claude / Gemini / Copilot, an AI image tool, generating copy/images/ideas, responsible AI use, accuracy of claims, data privacy, ad-platform rules, disclosure",
 steps=[
 ("Using your brand voice and personas from Lab 3, generate a first batch of campaign ideas. Paste the prompt below.",
  "Using this brand voice [paste your Kopi Culture Co. voice attributes] and these personas [paste your three personas], give me ten campaign ideas for the Neighbourhood Series launch — a mix of organic social, email and small-budget paid — each as a one-line concept naming the persona it targets. Keep them on voice and realistic for a small brand."),
 ("Generate a short copy draft and a starter image so you see the loop on real deliverables. Paste the copy prompt into a chat assistant, then paste the image prompt into your AI image tool.",
  "Write a 50-word launch announcement for the Neighbourhood Series in the Kopi Culture Co. voice, for the young-urban-coffee-lover persona, ending with a clear call to action. Avoid clichés and do not invent awards or claims."),
 ("Generate the starter image. Paste this into your AI image tool and review it against the brand.",
  "Four premium drip-bag coffee sachets in a giftable box on a marble café table, warm natural light, modern minimal Singapore café aesthetic, no text and no logos, product photography, square 1:1."),
 ("Review the outputs with a critical eye: which idea is strongest for each persona, does the copy claim anything you can't back up, and does the image invent any odd detail? Note what you would keep and what you would fix — this is the generate–review–refine loop on real work.", ""),
 ("Ask AI to draft a responsible-use checklist for AI-assisted marketing. Paste the prompt below.",
  "You are a marketing ethics and compliance advisor. I am using generative AI to create a product launch campaign (copy, images, video, ads and email) for a small brand. Give me a practical, plain-language checklist for using AI responsibly — covering accuracy and not inventing statistics, awards or claims; originality and not imitating a real competitor's identity; keeping confidential and customer data out of public tools; following the advertising rules of Meta and Google; and being transparent about AI assistance. Keep each point to one line."),
 ("Decide Kopi Culture Co.'s position on the key questions and write a one-line answer for each: Will you publish any statistic or claim the AI produces without verifying it? (No.) Will you paste real customer data into a public AI tool? (No.) Will you imitate a real competitor's look or voice? (No.) Will you disclose AI assistance, and where? Will you check each ad against the platform's rules before it runs?", ""),
 ("Save your first campaign ideas, copy draft and image, your responsible-generation checklist and the brand's decisions in your project folder. These ground rules apply to every deliverable you create for the rest of the course.", ""),
 ],
 test="You have generated a first batch of on-voice campaign ideas, a short copy draft and a starter product image and reviewed them critically, and you have a responsible-generation checklist applied to the Neighbourhood Series — covering accuracy of claims, originality, data privacy, ad-platform rules and disclosure — with a decided position on each key question, all saved in your project folder.",
 ),
]
