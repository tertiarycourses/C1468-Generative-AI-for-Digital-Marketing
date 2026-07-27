# -*- coding: utf-8 -*-
"""
Domain 2 — Content Creation with Generative AI. Labs 5-8 (Day 1).

Lab 5 creates the social media content; Lab 6 writes the ad and email copy;
Lab 7 generates the on-brand images and short-form video; Lab 8 runs a
brand-consistency pass and repurposes one core piece across every channel. Each
lab holds its output to the brand voice and personas defined in Lab 3 and the
responsible-generation rules set in Lab 4.
"""

DOMAIN2 = [
 dict(
 num=5, topic=2,
 title="Create Social Media Content",
 objective="Use AI to create platform-appropriate social media content for the Neighbourhood Series — scroll-stopping hooks, captions, hashtags and post concepts for Instagram and TikTok — organised into a first content calendar.",
 desc="Social is where the launch earns attention. In this lab you use a chat assistant, on your Lab 3 voice "
 "and personas, to generate social content that fits how each platform actually works. You produce a set of "
 "post concepts for Instagram and TikTok aimed at the young-urban-coffee-lover persona, strong hooks (the first "
 "line that stops the scroll), full captions with a clear call to action, and relevant hashtags — then you "
 "adapt tone and format per platform (polished and visual for Instagram, fast and casual for TikTok). You review "
 "everything against the voice, cut the clichés, and organise the posts into a first two-week content calendar "
 "so the launch has a rhythm rather than a pile of random posts. " + \
 "BUILDING BLOCK — what you create in this lab becomes part of your Neighbourhood Series campaign and AI Marketing Playbook, the connected campaign you assemble across all 16 labs.",
 build="A set of Instagram and TikTok post concepts for the launch — each with a hook, a full on-voice caption, a call to action and hashtags — adapted per platform and organised into a first two-week content calendar, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, social content, hooks and captions, hashtags, platform adaptation (Instagram, TikTok), a content calendar",
 steps=[
 ("Open your brand voice guide and personas from Lab 3. Ask AI for a batch of social post concepts. Paste the prompt below.",
  "Using this Kopi Culture Co. voice [paste voice] and targeting young urban coffee lovers (25-38) on Instagram and TikTok, give me eight social post concepts to launch the Neighbourhood Series (four local-flavour drip-bag coffees). For each: a one-line concept, the format (Reel, carousel, single image), and which of the four coffees it features. Keep them on voice and realistic for a small brand."),
 ("Turn the best concepts into full posts. Paste the prompt below.",
  "For three of those concepts, write the full post: a scroll-stopping first-line hook, a caption of 40-80 words in the Kopi Culture Co. voice with a clear call to action, and 8-12 relevant hashtags mixing branded, local and coffee tags. Avoid clichés like 'game-changer' and 'must-try'."),
 ("Adapt for each platform. Paste the prompt below and compare the two versions.",
  "Take one of those posts and give me two versions: an Instagram version (polished, aesthetic, slightly longer caption) and a TikTok version (fast, casual, punchy, hook in the first two seconds, script-style). Keep the same message and voice; change only tone, length and format."),
 ("Review with a critical eye: does each hook actually earn a stop, is every caption on voice, and are the calls to action clear? Cut any cliché or claim you can't back up, and tighten the weakest caption.", ""),
 ("Ask AI to organise the posts into a calendar. Paste the prompt below.",
  "Organise these Neighbourhood Series posts into a two-week launch content calendar for Instagram and TikTok: give me a simple table with date, platform, post concept, format, the coffee featured, and the funnel stage (awareness, consideration or conversion). Assume launch day is the start of week one."),
 ("Save your social post concepts, the full posts, the platform variants and the two-week content calendar in your project folder. These are the social layer of your campaign.", ""),
 ],
 test="You have a set of Neighbourhood Series social posts — hooks, on-voice captions, calls to action and hashtags — with Instagram and TikTok variants, reviewed and cut for clichés, all organised into a two-week launch content calendar, saved in your project folder.",
 ),
 dict(
 num=6, topic=2,
 title="Write Ad and Email Copy",
 objective="Use AI to write conversion-focused ad copy (Meta and Google) and launch and nurture emails for the Neighbourhood Series — headline and body variations, subject lines and clear calls to action — on the brand voice.",
 desc="Ads and email are where attention turns into sales. In this lab you use a chat assistant, on your voice "
 "and personas, to write ad copy and email copy built to convert. You generate Meta ad variations (primary "
 "text, headlines and descriptions) around one clear message and call to action, and Google search ad copy "
 "(headlines and descriptions) for the launch, producing several variants to test rather than one. You then "
 "write the launch email (hook, value, proof-free honest copy, call to action) and a short welcome/nurture "
 "email for new subscribers to The KCC Club, each with subject-line and preview-text options that earn the "
 "open. You review everything against the voice and the responsible-use rules, checking that no claim is "
 "invented and every CTA is clear. " + \
 "BUILDING BLOCK — what you create in this lab becomes part of your Neighbourhood Series campaign and AI Marketing Playbook, the connected campaign you assemble across all 16 labs.",
 build="Meta and Google ad copy variations for the launch (headlines, primary text and descriptions built around one message and CTA), plus a launch email and a welcome/nurture email — each with subject-line and preview-text options — all on voice and checked against the responsible-use rules, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, ad copy (Meta, Google), headline and body variations, email copy, subject lines and preview text, calls to action",
 steps=[
 ("Generate Meta ad copy. Paste the prompt below.",
  "You are a performance-marketing copywriter. Using this Kopi Culture Co. voice [paste voice] and targeting young urban coffee lovers, write three Meta (Instagram/Facebook) ad variations to launch the Neighbourhood Series. For each give: primary text (max 125 words), a headline (max 40 characters) and a description (max 30 characters), built around one clear message and a single call to action ('Shop the launch'). Do not invent awards, ratings or claims."),
 ("Generate Google search ad copy. Paste the prompt below.",
  "Write Google search ad copy for the Neighbourhood Series launch: give me five headlines (max 30 characters each) and three descriptions (max 90 characters each) that I can mix and match, focused on local-flavour specialty drip-bag coffee and a clear call to action. Keep it on voice and truthful."),
 ("Write the launch email. Paste the prompt below.",
  "Write a launch email for the Neighbourhood Series in the Kopi Culture Co. voice for our subscriber list: a compelling subject line (plus two alternates) and preview text, then a short email with a hook, the story of the four neighbourhood-inspired coffees, and one clear call to action to shop the launch. Keep it under 200 words, warm and characterful, no invented claims."),
 ("Write a welcome/nurture email for new subscribers. Paste the prompt below.",
  "Write a short welcome email for someone who just subscribed to The KCC Club (our monthly coffee subscription): subject line plus preview text, a warm on-voice welcome, what to expect each month, and one gentle call to action to complete their first order or profile. Under 150 words."),
 ("Review every piece against the voice and the responsible-use rules from Lab 4: is each ad within the character limits, is every claim truthful, is each CTA single and clear, and do the subject lines earn the open without clickbait? Fix the weakest variant of each.", ""),
 ("Save your Meta and Google ad variations, the launch email and the welcome email (with subject-line options) in your project folder. These are the paid and email layers of your campaign.", ""),
 ],
 test="You have Meta and Google ad copy variations within their character limits, a launch email and a welcome/nurture email each with subject-line and preview-text options, all on voice, with single clear calls to action and no invented claims, reviewed against the responsible-use rules and saved in your project folder.",
 ),
 dict(
 num=7, topic=2,
 title="Generate On-Brand Images and Short-Form Video",
 objective="Use AI image and video tools to generate on-brand visuals for the Neighbourhood Series — a moodboard, hero and lifestyle product images, and a short-form video script and clip for Reels or TikTok — with effective prompts.",
 desc="Content needs to be seen, not just read. In this lab you use an AI image tool and an AI video tool to "
 "produce the campaign's visuals on one consistent look. You first generate a small moodboard to set the visual "
 "direction (warm natural light, modern Singapore café aesthetic, local textures), then write strong image "
 "prompts — naming subject, style, composition, lighting, palette, mood and aspect ratio — to generate a hero "
 "product image and a lifestyle image, iterating one element at a time to stay on brand. You then write a "
 "short-form video script (hook, three quick beats, call to action) for a Reel or TikTok and use an AI video "
 "tool to assemble a draft clip. You review every asset for off-brand drift, garbled text and fake logos, and "
 "keep only what is honest and on brand. " + \
 "BUILDING BLOCK — what you create in this lab becomes part of your Neighbourhood Series campaign and AI Marketing Playbook, the connected campaign you assemble across all 16 labs.",
 build="A small visual moodboard, an on-brand hero product image and a lifestyle image (each with its prompt), and a short-form video script with a draft AI-generated clip for Reels or TikTok — all reviewed for brand fit and honesty, saved in your project folder.",
 services="AI image tool (DALL·E, Firefly, Designer, Gemini, Canva), AI video tool (Canva, Gemini/Veo, text-to-video), image prompting, moodboards, short-form video scripting",
 steps=[
 ("Set the visual direction with a moodboard. Paste the prompt below into your AI image tool and generate a few reference frames.",
  "A moodboard of four reference images for a Singapore specialty-coffee brand launch: warm natural light, marble and light-wood café surfaces, modern minimal styling, subtle local textures (peranakan tile, kopitiam marble), earthy warm palette, calm editorial feel. No text, no logos."),
 ("Generate the hero product image with a full prompt. Paste the prompt below and review it.",
  "A premium giftable box of four drip-bag coffee sachets on a marble café table, warm morning light from the left, a cup of black coffee and a few coffee beans beside it, modern minimal Singapore café aesthetic, earthy warm palette, shallow depth of field, product photography, 1:1 square, no text and no logos."),
 ("Generate a lifestyle image and iterate one element at a time. Paste the prompt below, then change only one thing (lighting, or palette, or angle) and regenerate to learn what each word does.",
  "A young person in a bright modern Singapore apartment brewing a drip-bag coffee over a mug by a window, relaxed weekend morning mood, warm natural light, earthy palette, candid lifestyle photography, 4:5 portrait, no text and no logos."),
 ("Write a short-form video script. Paste the prompt below.",
  "Write a 20-second short-form video script (for a Reel or TikTok) to launch the Neighbourhood Series in the Kopi Culture Co. voice: a hook in the first two seconds, three quick beats introducing the four neighbourhood-inspired coffees, and a call to action. Give me the on-screen text, the voiceover/caption line for each beat, and a shot suggestion. Keep it fast and characterful."),
 ("Assemble a draft clip. In your AI video tool (Canva, Gemini/Veo or a text-to-video generator), use the script and your images to generate or assemble a rough 15-20 second clip in 9:16. It is a draft to feel the tool, not a finished ad.", ""),
 ("Review every visual asset: is it on brand and consistent with the moodboard, does the image have garbled text, a fake logo or a wrong product, and does the video read clearly with sound off? Regenerate anything off-brand and add real text on the slide/clip rather than trusting AI-rendered text.", ""),
 ("Save your moodboard, hero and lifestyle images (with their prompts), the video script and the draft clip in your project folder. These are the visual layer of your campaign.", ""),
 ],
 test="You have a moodboard, an on-brand hero product image and a lifestyle image (each with its prompt), and a short-form video script with a draft 9:16 clip — all reviewed and consistent with the visual direction, free of garbled text and fake logos — saved in your project folder.",
 ),
 dict(
 num=8, topic=2,
 title="Maintain Brand Voice and Consistency Across Channels",
 objective="Run an AI brand-consistency pass across everything created so far, and repurpose one core piece of content into every channel — so the whole Neighbourhood Series campaign sounds like one brand and carries one message.",
 desc="A campaign works only when every piece feels like the same brand. In this lab you consolidate the "
 "content from Labs 5-7 and use AI to enforce consistency. You give the AI your voice guide and paste in your "
 "social captions, ad copy and emails, and ask it to flag anything off-voice, off-message or inconsistent in "
 "key wording, then rewrite the flagged pieces back on voice. You then practise the most efficient content "
 "habit — repurposing — by taking one strong core piece (your launch announcement) and having AI atomise it "
 "into an Instagram caption, a TikTok script, a Meta ad, an email teaser and a LinkedIn post, each adapted for "
 "its channel while carrying the same message. By the end your campaign content is aligned, and you have a "
 "repeatable one-to-many repurposing workflow. " + \
 "BUILDING BLOCK — what you create in this lab becomes part of your Neighbourhood Series campaign and AI Marketing Playbook, the connected campaign you assemble across all 16 labs.",
 build="A brand-consistency report on your campaign content with the flagged pieces rewritten back on voice, plus one core piece repurposed into an Instagram caption, a TikTok script, a Meta ad, an email teaser and a LinkedIn post — a repeatable one-to-many repurposing workflow — saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, brand-consistency pass, voice alignment, content repurposing (one-to-many), channel adaptation",
 steps=[
 ("Gather your content from Labs 5-7 (social captions, ad copy, emails) into one document. Run a consistency pass with AI. Paste the prompt below along with your voice guide and the content.",
  "Here is my Kopi Culture Co. brand voice guide [paste] and a set of campaign content — social captions, ad copy and emails [paste]. Review all of it for consistency: flag anything that is off-voice, off-message, or uses different wording for the same thing (product names, the call to action, key phrases). Give me a short list of issues and the fix for each."),
 ("Rewrite the flagged pieces. Paste the prompt below.",
  "Rewrite the pieces you flagged so they are fully on the Kopi Culture Co. voice and use consistent product names and a consistent call to action, keeping each piece's original purpose and channel. Show the before and after for each."),
 ("Confirm the shared elements are locked: the four coffee names, the campaign name (Neighbourhood Series), the subscription name (The KCC Club) and the primary call to action are written the same way everywhere. Note any you standardised.", ""),
 ("Now practise repurposing. Take your launch announcement as the core piece and paste the prompt below.",
  "Here is one core piece of content — our Neighbourhood Series launch announcement [paste]. Repurpose it into five channel-specific pieces that all carry the same message and voice: (1) an Instagram caption, (2) a TikTok script, (3) a Meta ad primary text, (4) a one-line email teaser, and (5) a short LinkedIn post. Adapt tone, length and format for each channel; keep the message and the call to action consistent."),
 ("Review the repurposed set: does every piece carry the same core message and call to action while fitting its channel? Fix any that drifted, then note the repurposing prompt as a reusable workflow (one core piece in, five channel pieces out).", ""),
 ("Save your consistency report, the rewritten pieces and the repurposed one-to-many set (plus the reusable repurposing prompt) in your project folder. Your Day 1 content kit is now aligned and ready to plan and optimise on Day 2.", ""),
 ],
 test="You have a brand-consistency report with the flagged content rewritten back on voice and shared elements (coffee names, campaign name, subscription name, primary CTA) standardised, plus one core piece repurposed into five consistent channel-specific pieces and saved as a reusable repurposing workflow — all in your project folder.",
 ),
]
