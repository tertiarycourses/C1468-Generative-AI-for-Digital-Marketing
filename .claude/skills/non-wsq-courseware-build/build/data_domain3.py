# -*- coding: utf-8 -*-
"""
Domain 3 — Campaign Planning and Optimisation with AI. Labs 9-12 (Day 2).

Lab 9 researches audiences and keywords; Lab 10 plans the multi-channel campaign
and funnel; Lab 11 personalises and scales the content by segment; Lab 12 designs
and runs A/B tests and optimises. Each lab builds on the content kit from Day 1
and holds its output to the brand voice, personas and responsible-use rules.
"""

PROJECT_NOTE = (
 "BUILDING BLOCK — what you create in this lab becomes part of your Neighbourhood Series campaign and AI "
 "Marketing Playbook, the connected campaign you assemble across all 16 labs."
)

DOMAIN3 = [
 dict(
 num=9, topic=3,
 title="Research Audiences and Keywords",
 objective="Use AI to deepen the Neighbourhood Series audience research and to build keyword clusters for SEO and paid search — grounding the campaign in real customer language and search intent before you plan.",
 desc="Good marketing is built on research, not guesses. In this lab you use a chat assistant to sharpen your "
 "understanding of the audience and the search landscape. You take your three personas from Lab 3 and deepen "
 "them — goals, pain points, objections, the moments they buy coffee, the channels they use and the exact words "
 "they use — so your messaging speaks to real people. You then run keyword research: you prompt AI for seed "
 "keywords around specialty coffee, drip-bag coffee, local flavours and gifting, cluster them by theme and by "
 "search intent (informational, commercial, transactional), and map each cluster to content for SEO and to ad "
 "groups for paid search. You finish by noting that AI's volumes are estimates to verify in a real keyword "
 "tool. " + PROJECT_NOTE,
 build="Deepened audience research for the three personas (goals, pain points, objections, buying moments, channels and language) and a keyword map — seed keywords clustered by theme and search intent, mapped to SEO content and paid ad groups — saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, audience research, pain points and objections, keyword research, keyword clustering, search intent, SEO and paid mapping",
 steps=[
 ("Deepen your personas. Paste the prompt below along with your three personas from Lab 3.",
  "Here are my three Neighbourhood Series personas [paste]. For each, deepen the research: their goals when buying coffee, their top three pain points, the objections that stop them buying, the specific moments they buy or gift coffee, the channels where they discover brands, and ten exact words or phrases they use about coffee. Keep it concrete and realistic for Singapore."),
 ("Identify objections to handle in the campaign. Paste the prompt below.",
  "Based on those personas, list the five most likely objections to buying premium local-flavour drip-bag coffee (for example price, 'is drip-bag as good as fresh', gifting doubt) and, for each, one honest, on-voice message that addresses it without overclaiming."),
 ("Generate seed keywords. Paste the prompt below.",
  "Generate a list of 30 seed keywords a Singapore specialty-coffee brand could target for the Neighbourhood Series launch, covering specialty coffee, drip-bag coffee, local-flavour coffee (gula melaka, kaya, teh tarik, pandan), coffee subscription and coffee gifting. Mix short head terms and longer specific phrases."),
 ("Cluster the keywords by theme and intent. Paste the prompt below.",
  "Cluster those keywords into 5-7 themes, and label each keyword's likely search intent (informational, commercial or transactional). Then, in a simple table, map each cluster to: a content idea for SEO (a blog or landing page), and an ad group for paid search. Note which clusters are best for organic vs paid."),
 ("Sanity-check and verify: note in one line that the search volumes and competition are estimates you will confirm in a real keyword tool (Google Keyword Planner or similar), and flag any keyword that feels off for Singapore or the brand.", ""),
 ("Save your deepened personas, the objection-handling messages, and the clustered keyword map (with SEO and paid mapping) in your project folder. This research grounds the campaign plan in Lab 10.", ""),
 ],
 test="You have deepened audience research for all three personas (with buying moments, channels, exact language and handled objections) and a keyword map — 30+ seed keywords clustered into themes, labelled by search intent and mapped to SEO content and paid ad groups, with a note to verify volumes — saved in your project folder.",
 ),
 dict(
 num=10, topic=3,
 title="Plan a Multi-Channel Campaign",
 objective="Use AI to turn the research and content into a complete multi-channel campaign plan for the Neighbourhood Series — objectives, funnel stages, channel mix, content map and a realistic, budget-aware timeline and calendar.",
 desc="A campaign is a plan, not a pile of posts. In this lab you use a chat assistant to assemble everything "
 "so far — voice, personas, keyword research and the Day 1 content kit — into one coherent multi-channel plan. "
 "You set clear objectives and a headline metric, then map content to the marketing funnel: awareness "
 "(organic social, short-form video), consideration (SEO content, email, retargeting), conversion (ads, launch "
 "email, offers) and retention (subscription nurture, WhatsApp). You choose the channel mix and weight it for a "
 "small-brand budget — favouring organic social, email and SEO over big-spend media — and build a realistic "
 "launch timeline and a week-by-week calendar that ties the existing content to funnel stages and channels. By "
 "the end you have a plan you could actually run. " + PROJECT_NOTE,
 build="A complete multi-channel campaign plan for the Neighbourhood Series — objectives and headline metric, a funnel map (awareness, consideration, conversion, retention) with content and channels per stage, a budget-aware channel mix, and a week-by-week launch timeline and calendar — saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, campaign planning, marketing funnel, channel mix, content mapping, budget-aware planning, timeline and calendar",
 steps=[
 ("Set the objectives. Paste the prompt below.",
  "You are a marketing strategist. For the Kopi Culture Co. Neighbourhood Series launch (four local-flavour drip-bag coffees plus The KCC Club subscription, small-brand budget, year-end season, personas: young urban coffee lovers, busy WFH professionals, gift shoppers), define: one primary objective, two supporting objectives, and one headline metric to judge success. Keep them specific and realistic."),
 ("Map content to the funnel. Paste the prompt below.",
  "Map the Neighbourhood Series campaign to the marketing funnel. For each stage — awareness, consideration, conversion, retention — give: the goal, the best channels, the content types (I already have social posts, ads, emails, images and a video), and the persona focus. Present it as a table."),
 ("Choose and weight the channel mix. Paste the prompt below.",
  "Recommend a channel mix for a small-brand budget across organic Instagram and TikTok, SEO/blog, email, a modest Meta ads budget and a small Google search budget. Suggest a rough percentage of effort/budget per channel, favouring high-leverage low-cost channels, and justify each in one line. Flag anything I should not spend on yet."),
 ("Build the timeline and calendar. Paste the prompt below.",
  "Build a four-week launch timeline for the Neighbourhood Series: a week-by-week plan (pre-launch teaser, launch week, sustain, gifting push) showing what publishes on which channel and which funnel stage it serves, tying in my existing content calendar. Present it as a simple week-by-week table."),
 ("Review the plan against reality: is every stage covered, does the budget favour low-cost high-leverage channels, and is the timeline achievable for a small team? Adjust anything unrealistic and note the one thing most likely to drive results.", ""),
 ("Save your objectives, funnel map, channel mix and launch timeline/calendar as the Neighbourhood Series campaign plan in your project folder. Labs 11 and 12 personalise, scale and optimise this plan.", ""),
 ],
 test="You have a complete multi-channel campaign plan — objectives and a headline metric, a funnel map with content and channels per stage, a budget-aware channel mix with rough weighting, and a week-by-week launch timeline and calendar tied to your content — saved in your project folder.",
 ),
 dict(
 num=11, topic=3,
 title="Personalise and Scale Content",
 objective="Use AI to personalise the campaign message for each persona and segment, and to produce on-brand variants at scale — segmented emails, per-audience ad sets and localised captions — without losing the brand voice.",
 desc="One message rarely fits every customer. In this lab you use a chat assistant to tailor the campaign to "
 "each persona and then to scale that tailoring efficiently. You take one core offer and personalise it three "
 "ways — for young urban coffee lovers, busy WFH professionals and gift shoppers — changing the framing, the "
 "benefit and the call to action while keeping the message and voice consistent. You then scale: you generate a "
 "segmented email variant per persona, a per-audience ad set (different hook per persona, same offer), and a "
 "set of caption variants, all in one structured pass. Crucially, you hold every variant to the brand voice and "
 "the responsible-use rules, so scaling means more relevant content, not more noise. You finish by defining a "
 "simple rule for which variant goes to which segment. " + PROJECT_NOTE,
 build="The core offer personalised for all three personas, plus scaled on-brand variants — a segmented email per persona, a per-audience ad set, and caption variants — with a simple segment-to-variant mapping, all held to the brand voice, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, personalisation, segmentation, content variants at scale, message consistency, voice control",
 steps=[
 ("Personalise the core offer three ways. Paste the prompt below.",
  "Here is one core offer for the Neighbourhood Series launch [paste your launch message and offer]. Personalise it for each of my three personas — young urban coffee lovers, busy WFH professionals, and gift shoppers — changing the framing, the main benefit emphasised, and the call to action for each, while keeping the same core message and the Kopi Culture Co. voice. Show the three versions side by side."),
 ("Scale to segmented emails. Paste the prompt below.",
  "Write a launch email variant for each of the three personas: same offer and voice, but a persona-specific subject line, opening hook and main benefit. Keep each under 160 words with one clear call to action. Note in one line what changed for each segment."),
 ("Scale to a per-audience ad set. Paste the prompt below.",
  "Create a Meta ad set with one ad per persona for the launch: same offer and single call to action, but a persona-specific hook and primary text (max 100 words each). Give the three ads and a one-line audience-targeting note for each (interests/behaviours that match that persona)."),
 ("Generate caption variants at scale, then hold the line on voice. Paste the prompt below.",
  "Give me six on-voice caption variants for the launch that I can rotate across social posts — vary the angle (origin story, gifting, convenience, flavour, subscription value, local pride) but keep the same voice, message and call to action. Then check all six against this voice guide [paste] and flag any that drifted."),
 ("Define the routing rule and review: write a simple mapping of which variant goes to which segment/channel, and confirm every scaled variant is on voice, truthful and non-repetitive. Cut or fix any weak or off-voice variant — scale should raise relevance, not noise.", ""),
 ("Save your personalised core offer, the segmented emails, the per-audience ad set, the caption variants and the segment-to-variant mapping in your project folder. This personalised, scaled content feeds the A/B tests in Lab 12.", ""),
 ],
 test="You have the core offer personalised for all three personas and scaled on-brand variants — a segmented email per persona, a per-audience ad set with targeting notes, and six checked caption variants — plus a simple segment-to-variant mapping, all held to the brand voice and saved in your project folder.",
 ),
 dict(
 num=12, topic=3,
 title="A/B Test and Optimise",
 objective="Use AI to design and run A/B tests on the campaign's key elements — subject lines, ad headlines, hooks and CTAs — with clear hypotheses and metrics, then interpret the results and optimise with the winners.",
 desc="You improve marketing by testing, not guessing. In this lab you use a chat assistant to turn your "
 "content into structured experiments. You pick the highest-leverage elements to test — an email subject line, "
 "an ad headline, a social hook and a call to action — and for each you write a clear hypothesis, define the "
 "single metric that decides the winner (open rate, click-through rate, conversion), and generate two "
 "meaningfully different variants (A and B) to compare. You then work with realistic sample results: you paste "
 "in example numbers for a subject-line test, and AI helps you read which variant won, whether the difference "
 "is meaningful, and what to try next — feeding the learning into the following round. By the end you have a "
 "small test plan and the habit of continuous optimisation. " + PROJECT_NOTE,
 build="A/B test designs for the campaign's key elements — each with a hypothesis, the deciding metric and two variants — plus a worked interpretation of a sample subject-line test result and the next optimisation to try, saved in your project folder.",
 services="ChatGPT / Claude / Gemini / Copilot, A/B testing, hypotheses, test metrics, variant generation, interpreting results, optimisation loop",
 steps=[
 ("Choose what to test and why. Paste the prompt below.",
  "For the Neighbourhood Series launch, recommend the four highest-leverage elements to A/B test first (across email, ads and social) for a small brand, and for each explain in one line why testing it is worth the effort and which single metric should decide the winner."),
 ("Design the tests with hypotheses. Paste the prompt below.",
  "For each of these four elements — an email subject line, a Meta ad headline, a social hook, and a call-to-action button label — write an A/B test: a one-sentence hypothesis ('If we ... then ... because ...'), the deciding metric, and two meaningfully different variants A and B (not just reworded). Keep everything on the Kopi Culture Co. voice."),
 ("Interpret a sample result. Paste the prompt below with the example numbers.",
  "Here are results from my subject-line A/B test. Variant A: sent 1,000, opens 220 (22%). Variant B: sent 1,000, opens 265 (26.5%). Click-throughs: A 40, B 38. Which subject line won on the deciding metric (open rate), is the difference meaningful for this sample size, and what does the click-through difference suggest I should test next? Explain simply."),
 ("Decide and plan the next round. Paste the prompt below.",
  "Based on that result, recommend the next single test to run to improve clicks (not just opens), with a hypothesis, the metric, and two variants. Explain why changing one element at a time matters for learning."),
 ("Review and record the discipline: confirm each test changes only one element, has one deciding metric, and keeps the winner; note that real significance needs adequate sample size and that you verify numbers before acting. Write your testing rule in one line.", ""),
 ("Save your A/B test designs, the worked interpretation and your next-round plan in your project folder. This optimisation habit carries into the analytics work in Lab 13.", ""),
 ],
 test="You have A/B test designs for four key elements (each with a hypothesis, deciding metric and two distinct variants), a correct interpretation of the sample subject-line test (Variant B won on open rate), a next-round test to improve clicks, and your one-line testing rule — all saved in your project folder.",
 ),
]
