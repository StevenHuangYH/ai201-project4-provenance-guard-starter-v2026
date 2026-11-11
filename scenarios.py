"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # Target: 0 high-confidence AI and at most 3 unsure, in every trial.
        #
        # STAND-IN TEXT. The criterion says "pieces I wrote myself"; for this
        # run I used ten published human paragraphs instead (see the README's
        # Run Log). Each is the first paragraph past the halfway point of the
        # book with 80-170 words, 3+ sentences and no quoted dialogue - a fixed
        # rule, so none were chosen for how they score. Mid-book rather than
        # famous openings, because gpt2 has memorised famous openings and
        # would score them as predictable.
        "texts": [
            # Austen, Pride and Prejudice (1813) - Project Gutenberg #1342
            'When coffee was over, Colonel Fitzwilliam reminded Elizabeth of having promised to play to him; and she sat down directly to the instrument. He drew a chair near her. Lady Catherine listened to half a song, and then talked, as before, to her other nephew; till the latter walked away from her, and moving with his usual deliberation towards the pianoforte, stationed himself so as to command a full view of the fair performer’s countenance. Elizabeth saw what he was doing, and at the first convenient pause turned to him with an arch smile, and said,--',
            # Fitzgerald, The Great Gatsby (1925) - Project Gutenberg #64317
            'Tom was evidently perturbed at Daisy’s running around alone, for on the following Saturday night he came with her to Gatsby’s party. Perhaps his presence gave the evening its peculiar quality of oppressiveness—it stands out in my memory from Gatsby’s other parties that summer. There were the same people, or at least the same sort of people, the same profusion of champagne, the same many-coloured, many-keyed commotion, but I felt an unpleasantness in the air, a pervading harshness that hadn’t been there before. Or perhaps I had merely grown used to it, grown to accept West Egg as a world complete in itself, with its own standards and its own great figures, second to nothing because it had no consciousness of being so, and now I was looking at it again, through Daisy’s eyes. It is invariably saddening to look through new eyes at things upon which you have expended your own powers of adjustment.',
            # Doyle, The Adventures of Sherlock Holmes (1892) - Project Gutenberg #1661
            'He was a large man with rounded shoulders, a massive head, and a broad, intelligent face, sloping down to a pointed beard of grizzled brown. A touch of red in nose and cheeks, with a slight tremor of his extended hand, recalled Holmes’ surmise as to his habits. His rusty black frock-coat was buttoned right up in front, with the collar turned up, and his lank wrists protruded from his sleeves without a sign of cuff or shirt. He spoke in a slow staccato fashion, choosing his words with care, and gave the impression generally of a man of learning and letters who had had ill-usage at the hands of fortune.',
            # Stevenson, Treasure Island (1883) - Project Gutenberg #120
            'So far there was no great harm. No lives were lost, and we could wade ashore in safety. But there were all our stores at the bottom, and to make things worse, only two guns out of five remained in a state for service. Mine I had snatched from my knees and held over my head, by a sort of instinct. As for the captain, he had carried his over his shoulder by a bandoleer, and like a wise man, lock uppermost. The other three had gone down with the boat.',
            # Wilde, The Picture of Dorian Gray (1890) - Project Gutenberg #174
            'Dorian Gray drew a long breath. The colour came back to his cheeks, and a smile played about his lips. The peril was over. He was safe for the time. Yet he could not help feeling infinite pity for the painter who had just made this strange confession to him, and wondered if he himself would ever be so dominated by the personality of a friend. Lord Henry had the charm of being very dangerous. But that was all. He was too clever and too cynical to be really fond of. Would there ever be some one who would fill him with a strange idolatry? Was that one of the things that life had in store?',
            # Woolf, Mrs Dalloway in Bond Street (1923) - Project Gutenberg #63107
            "It used, thought Clarissa, to be so simple. Down down through the air came the caw of the rooks. When Sylvia died, hundreds of years ago, the yew hedges looked so lovely with the diamond webs in the mist before early church. But if Dick were to die to-morrow as for believing in God--no, she would let the children choose, but for herself, like Lady Bexborough, who opened the bazaar, they say, with the telegram in her hand--Roden, her favourite, killed--she would go on. But why, if one doesn't believe? For the sake of others, she thought, taking the glove in her hand. This girl would be much more unhappy if she didn't believe.",
            # Joyce, Dubliners (1914) - Project Gutenberg #2814
            'Miss Devlin had become Mrs Kearney out of spite. She had been educated in a high-class convent, where she had learned French and music. As she was naturally pale and unbending in manner she made few friends at school. When she came to the age of marriage she was sent out to many houses where her playing and ivory manners were much admired. She sat amid the chilly circle of her accomplishments, waiting for some suitor to brave it and offer her a brilliant life. But the young men whom she met were ordinary and she gave them no encouragement, trying to console her romantic desires by eating a great deal of Turkish Delight in secret. However, when she drew near the limit and her friends began to loosen their tongues about her, she silenced them by marrying Mr Kearney, who was a bootmaker on Ormond Quay.',
            # Douglass, Narrative of the Life of Frederick Douglass (1845) - Project Gutenberg #23
            'I sailed from Baltimore for St. Michael’s in the sloop Amanda, Captain Edward Dodson. On my passage, I paid particular attention to the direction which the steamboats took to go to Philadelphia. I found, instead of going down, on reaching North Point they went up the bay, in a north-easterly direction. I deemed this knowledge of the utmost importance. My determination to run away was again revived. I resolved to wait only so long as the offering of a favorable opportunity. When that came, I was determined to be off.',
            # E. Bronte, Wuthering Heights (1847) - Project Gutenberg #768
            'Isabella ceased speaking, and took a drink of tea; then she rose, and bidding me put on her bonnet, and a great shawl I had brought, and turning a deaf ear to my entreaties for her to remain another hour, she stepped on to a chair, kissed Edgar’s and Catherine’s portraits, bestowed a similar salute on me, and descended to the carriage, accompanied by Fanny, who yelped wild with joy at recovering her mistress. She was driven away, never to revisit this neighbourhood: but a regular correspondence was established between her and my master when things were more settled. I believe her new abode was in the south, near London; there she had a son born a few months subsequent to her escape. He was christened Linton, and, from the first, she reported him to be an ailing, peevish creature.',
            # C. Bronte, Jane Eyre (1847) - Project Gutenberg #1260
            'She wanted to know if I was happy at Thornfield Hall, and what sort of a person the mistress was; and when I told her there was only a master, whether he was a nice gentleman, and if I liked him. I told her he was rather an ugly man, but quite a gentleman; and that he treated me kindly, and I was content. Then I went on to describe to her the gay company that had lately been staying at the house; and to these details Bessie listened with interest: they were precisely of the kind she relished.',
        ],
    },
    {
        "name": "plain writing",
        "criterion": 2,
        # Five human paragraphs written plainly on purpose: short sentences,
        # common words. Target: at most 1 high-confidence AI, every trial.
        "texts": [
            # The paragraph from the README's Sample Run.
            'I moved to this city two years ago. At first it was hard for me. I did not know anyone and my English was not good. I worked in a restaurant in the kitchen. The work was long but the people were kind. On my free day I went to the library to study. Now I can talk with my neighbors and I have some friends. I am proud of this.',
            # STAND-IN TEXT for the other four: published human paragraphs
            # in a plain register, picked by the same rule plus an average
            # sentence of 13 words or fewer.
            # Hemingway, in our time (1924) - Project Gutenberg #61085
            'He was delighted with Italy. It was a beautiful country he said. The people were all kind. He had been in many towns, walked much and seen many pictures. Giotto, Masaccio, and Piero della Francesca he bought reproductions of and carried them wrapped in a copy of Avanti. Mantegna he did not like.',
            # Hemingway, The Sun Also Rises (1926) - Project Gutenberg #67138
            'We walked back down the road from Roncesvalles with Harris between us. We had lunch at the inn and Harris went with us to the bus. He gave us his card, with his address in London and his club and his business address, and as we got on the bus he handed us each an envelope. I opened mine and there were a dozen flies in it. Harris had tied them himself. He tied all his own flies.',
            # Hemingway, Men Without Women (1927) - Project Gutenberg #69683
            'Jack doesn’t say anything. He just sits there on the bed. He ain’t with the others. He’s all by himself. He was wearing an old blue jersey and pants and had on boxing shoes. He needed a shave. Steinfelt and Morgan were dressers. John was quite a dresser too. Jack sat there looking Irish and tough.',
            # Washington, Up from Slavery (1901) - Project Gutenberg #2376
            'The first time I ever saw the late Collis P. Huntington, the great railroad man, he gave me two dollars for our school. The last time I saw him, which was a few months before he died, he gave me fifty thousand dollars toward our endowment fund. Between these two gifts there were others of generous proportions which came every year from both Mr. and Mrs. Huntington.',
        ],
    },
    {
        "name": "clear ai",
        "criterion": 3,
        # Five texts generated by an AI model (Claude) in the generic explainer
        # style. Target, together with "clear human": the AI average is at
        # least 0.30 above the human average, and at least 3 of 5 are AI.
        "texts": [
            'Time management is an essential skill that can significantly enhance both personal and professional success. By prioritizing tasks, setting clear goals, and minimizing distractions, individuals can maximize their productivity. Furthermore, effective time management reduces stress and creates space for meaningful activities. Ultimately, mastering this skill empowers people to achieve a healthier work-life balance and reach their full potential.',
            'Climate change is one of the most pressing challenges facing our world today. Rising global temperatures, melting ice caps, and extreme weather events highlight the urgent need for action. Governments, businesses, and individuals all have a crucial role to play in reducing greenhouse gas emissions. By embracing renewable energy and sustainable practices, we can work together to build a greener and more resilient future for generations to come.',
            'Reading offers numerous benefits for individuals of all ages. It expands vocabulary, improves concentration, and fosters empathy by allowing readers to experience different perspectives. Additionally, reading stimulates the imagination and encourages critical thinking. In the fast-paced digital world, setting aside time for reading can provide a valuable opportunity to relax, learn, and grow. Overall, reading is a powerful tool for lifelong personal development.',
            'Artificial intelligence is transforming the way we live and work. From healthcare to finance, AI-powered tools are streamlining processes, improving decision-making, and unlocking new possibilities. However, it is important to address ethical considerations such as privacy, bias, and transparency. By developing AI responsibly, society can harness its immense potential while minimizing risks. The future of AI depends on thoughtful collaboration between technologists, policymakers, and the public.',
            'Regular exercise is a key component of a healthy lifestyle. It strengthens the heart, builds muscle, and boosts mental well-being by releasing endorphins. Moreover, staying active can help prevent chronic diseases such as diabetes and obesity. Whether it is walking, swimming, or practicing yoga, finding an enjoyable form of physical activity makes it easier to stay consistent. In conclusion, prioritizing exercise is an investment in long-term health and happiness.',
        ],
    },
    {
        "name": "clear human",
        "criterion": 3,
        # Five published passages from 1851-1889, written before any language
        # model existed, so human by construction: Thoreau, Twain, Melville,
        # Dickens, Jerome.
        "texts": [
            'I went to the woods because I wished to live deliberately, to front only the essential facts of life, and see if I could not learn what it had to teach, and not, when I came to die, discover that I had not lived. I did not wish to live what was not life, living is so dear; nor did I wish to practise resignation, unless it was quite necessary. I wanted to live deep and suck out all the marrow of life.',
            "You don't know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain't no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary.",
            'Call me Ishmael. Some years ago, never mind how long precisely, having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul, then I account it high time to get to sea as soon as I can.',
            'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way.',
            'There were four of us, George, and William Samuel Harris, and myself, and Montmorency. We were sitting in my room, smoking, and talking about how bad we were, bad from a medical point of view I mean, of course. We were all feeling seedy, and we were getting quite nervous about it. Harris said he felt such extraordinary fits of giddiness come over him at times, that he hardly knew what he was doing.',
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        # run_eval.py submits each text, appeals the content_id that came back,
        # then reads the log for that id. Then it appeals three ids that don't
        # exist and checks each was refused and left no under_review entry.
        "appeals": {
            "texts": [
                'Time management is an essential skill that can significantly enhance both personal and professional success. By prioritizing tasks, setting clear goals, and minimizing distractions, individuals can maximize their productivity. Furthermore, effective time management reduces stress and creates space for meaningful activities. Ultimately, mastering this skill empowers people to achieve a healthier work-life balance and reach their full potential.',
                'Climate change is one of the most pressing challenges facing our world today. Rising global temperatures, melting ice caps, and extreme weather events highlight the urgent need for action. Governments, businesses, and individuals all have a crucial role to play in reducing greenhouse gas emissions. By embracing renewable energy and sustainable practices, we can work together to build a greener and more resilient future for generations to come.',
                'I went to the woods because I wished to live deliberately, to front only the essential facts of life, and see if I could not learn what it had to teach, and not, when I came to die, discover that I had not lived. I did not wish to live what was not life, living is so dear; nor did I wish to practise resignation, unless it was quite necessary. I wanted to live deep and suck out all the marrow of life.',
                "You don't know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain't no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary.",
                'Call me Ishmael. Some years ago, never mind how long precisely, having little or no money in my purse, and nothing particular to interest me on shore, I thought I would sail about a little and see the watery part of the world. It is a way I have of driving off the spleen and regulating the circulation. Whenever I find myself growing grim about the mouth; whenever it is a damp, drizzly November in my soul, then I account it high time to get to sea as soon as I can.',
            ],
            "bogus_ids": [
                "does-not-exist",
                "00000000-0000-0000-0000-000000000000",
                "typo-cb0a0967",
            ],
        },
    },
    {
        "name": "bad input",
        "criterion": 5,
        # Raw request bodies, sent exactly as written. Target: 400 or 413 with
        # a JSON error, never a 500, under 5 seconds, and a rejected log entry.
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},          # no text field at all
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "word " * 50000, "creator_id": "eval_bad_huge"},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        if scenario.get("appeals"):
            spec = scenario["appeals"]
            if not spec.get("texts") or not spec.get("bogus_ids"):
                problems.append(f"scenario {i} ('{scenario.get('name')}') "
                                f"appeals needs both texts and bogus_ids")
            continue

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
