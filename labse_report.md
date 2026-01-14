# 翻译质量评估报告 (LaBSE 语义相似度)

- 原文文件: `/home/cyw/pro/train_data/test_0429.txt`
- liquid 文件: `/home/cyw/pro/outlq_notune.txt`
- qwen 文件: `/home/cyw/pro/outqw_notune.txt`
- LaBSE 模型: `sentence-transformers/LaBSE`
- device: `cpu`

## 统计

- liquid 平均得分: 0.7355
- qwen 平均得分: 0.1235
- liquid 优于 qwen: 493
- qwen 优于 liquid: 7
- 平手: 0
- 参与统计句子数: 500

## 明细对比表

| 序号 | 日语原文 | liquid翻译 | liquid得分 | qwen翻译 | qwen得分 | 优胜方 |
|---:|---|---|---:|---|---:|---|
| 1 | 04/28T09:50:02 Event 7fe4/0420/6cc5 フジテレビ 081 | 04/28T09:50:02 Event 7fe4/0420/6cc5 Fuji TV 081 | 0.9086 | Friday, April 28 at 9:50 PM, Event 7FE4/0420/6CC5 FJTV 081 | 0.6748 | liquid |
| 2 | 04/28（月）09:50:00～11:30:00 | Mon. 28th, 04/28th (Monday) 9:50:00-11:30:00 | 0.8690 | 04/28 (Mon) 09:50:00 - 11:30:00 | 0.9451 | qwen |
| 3 | ノンストップ！【ニコニコ超会議に降臨小林幸子密着▽出演三浦大知３児パパ素顔】 | Non-stop! [Kobayashi Sachiko Descends on the Niconico Super Conference in a Secret Retreat▽Miura Daichi's 3 Children's Daddy's True Face]�������� | 0.7913 | "Non-stop! [Kikakunin Kakeba no Neko Super Meeting] - Minato Higuchi's focus, with Toshio Nakamura's three-year-old son playing a child-like face." | 0.6380 | liquid |
| 4 | ニコニコ超会議に降臨小林幸子密着▽「一時は死を覚悟…」ささきいさおが復帰ライブ▽三浦大知スタジオ登場３児パパ素顔▽向井理 | The Kimio Kobayashi Close-Up on the Nico Nico Super Conference ▽ "At One Point I Was Resigned to Death..." Isao Sasaki's Return Live ▽ Miura Daichi Studio Appearance 3 Children's Papa True Face ▽ Osamu Mukai | 0.8186 | Nico Cruise Conference arrives, focusing on Lina Otsuka's focus: "At first I was thinking of death…" Shizuka Ikeda returns in live broadcast at Tsurugaoka Studio, and three-year-old fatherless children appear with a childlike face. | 0.6830 | liquid |
| 5 | === Caption: , jpn | === C鉛筆: , jpn | 0.6872 | Caption: , japanese | 0.6215 | liquid |
| 6 | 04/28T09:50:02 === language: jpn | 04/28T09:50:02 McCall's English Language Course (Japanese) 04/28T09:50:02 Microsoft Windows & Mac OS X Version 10.5.0.0 (LTS) | 0.4860 | 04:28:09:02 === language: en | 0.7866 | qwen |
| 7 | 04/28T09:50:05 === language: --- | 04/28T09:50:05 英語 (日本時間 2005年2月28日) プロの翻訳家として活動しております。 訳文なしの翻訳書を完成させることのみを目的として翻訳作業を行っておりますので、説明や補足事項のない翻訳書をそのまま出力するのみで結構です。 | 0.3580 | 14:28:05 === time: | 0.5834 | qwen |
| 8 | 04/28T09:50:05 === language: --- | 04/28T09:50:05 英語 (日本時間 2005年2月28日) プロの翻訳家として活動しております。 訳文なしの翻訳書を完成させることのみを目的として翻訳作業を行っておりますので、説明や補足事項のない翻訳書をそのまま出力するのみで結構です。 | 0.3580 | 14:28:05 === time: | 0.5834 | qwen |
| 9 | 04/28T09:50:05 === language: jpn | 04/28T09:50:05 翻訳者:YOU - Professional translator. Translate the user's text into English. Only output the translation without any explanations or extra commentary. | 0.4657 | 14:28:05 === language: en | 0.6757 | qwen |
| 10 | 04/28T09:50:16 ≫おはようございます。 | 04/28T09:50:16 ≫Good morning.≫ You are a professional translator. Translate your text to English. | 0.6886 | Good morning! | 0.3743 | liquid |
| 11 | 04/28T09:50:19 ≫「ノンストップ！」始まりました。 | 04/28T09:50:19 ≫"Non-stop!" Has begun. | 0.9460 | "Non-stop!" started at 04:28 UTC+09:50. | 0.6947 | liquid |
| 12 | 04/28T09:50:21 ≫今週のせきららボイスの投稿テーマは | 04/28T09:50:21 ≫This week's theme for Sekirara Voice posts is... | 0.8385 | Sunday's Sukiya Voice post theme is | 0.4155 | liquid |
| 13 | 04/28T09:50:24 思い出のＧＷです。 | It's a memorable Golden Week letter. It's a GW letter from you. | 0.3857 | Dreams of Gw have been born. | 0.2450 | liquid |
| 14 | 04/28T09:50:27 表示されているＱＲコードから皆さん、ぜひ投稿してください。 | Please submit your entries from the QR code displayed on the screen. | 0.5692 | Please send your QR code images to everyone, please! | 0.4714 | liquid |
| 15 | 04/28T09:50:30 それでは参りましょうか。 | 04/28T09:50:30 Let's get started then? | 0.8714 | Sure, here is the translation from Japanese to English: | 0.1446 | liquid |
| 16 | 04/28T09:50:32 ≫４月２８日、今日も…。≫「ノンストップ！」。 | 04/28 T09:50:32 ≫April 28th, again…≫“Non-stop!” | 0.8563 | "Okay, do you want to come over?" | 0.1885 | liquid |
| 17 | 04/28T09:50:38 ≫先週金曜日、「パリピ孔明ＴＨＥ　ＭＯＶＩＥ」の | 04/28T09:50:38 ≫Last Friday, you appeared on "Pali Pi Kongming THE HEGGLE" | 0.7960 | "Today, too." | 0.1109 | liquid |
| 18 | 04/28T09:50:40 初日舞台あいさつが行われ | 04/28T09:50:40 First day of the stage greeting was held. | 0.8457 | Thursday, April 28 at 10:50 AM, before Monday, "The Paris Pupil's T.H.E. MOVIE" was released. | 0.4042 | liquid |
| 19 | 04/28T09:50:47 向井理さん、上白石萌歌さんディーン・フジオカさん | Rie Mukai, Moka Kamishiraishi, and Dean Fujioka. | 0.4314 | The opening ceremony of the first day was held at 10:50 AM. | 0.0866 | liquid |
| 20 | 04/28T09:50:48 宮野真守さんらが登場しました。 | 04/28T09:50:48 Yuichi Miyano and others appeared. [#1289] [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. [#1289] Makoto Miyano and others appeared. | 0.5967 | Tomoyuki Sato, Akiko Yamaguchi | 0.3657 | liquid |
| 21 | 04/28T09:50:53 ≫音楽で戦うことになりました。≫マジで！？ | 04/28T09:50:53 ≫The battle began with music. ≫Seriously!? | 0.8434 | The Shinsengumi forces were present. | -0.0109 | liquid |
| 22 | 04/28T09:50:59 ≫向井さん演じる諸葛孔明が現代に転生し | 04/28T09:50:59 ≫The Zhuge Liang portrayed by Mr. Mukai is reincarnated in modern times. | 0.7914 | Music is a game. Wow! | 0.0041 | liquid |
| 23 | 04/28T09:51:03 上白石さん演じるアマチュアシンガー、英子の | 04/28T09:51:03 The amateur singer Eiko, played by Ms. Shiraishi, reads the text for "Eiko the Amateur" | 0.7310 | The character of Zhuge Liang, played by Takeshi Kitano, has undergone a transformation into a modern-day figure. | 0.1881 | liquid |
| 24 | 04/28T09:51:07 軍師となって音楽の力で天下泰平を目指す | 04/28T09:51:07 Military Advisor Aiming for Peace Through the Power of Music | 0.8009 | A solo singer, English girl, 28 years old. | 0.1873 | liquid |
| 25 | 04/28T09:51:09 ド派手エンターテインメント映画です。 | 04/28T09:51:09 This is a flashy entertainment movie. | 0.8660 | The soldiers will use their military power to achieve a peaceful world. | -0.0169 | liquid |
| 26 | 04/28T09:51:17 「ノンストップ！」は向井さんや上白石さんら | 04/28T09:51:17 "Non-stop!" by Mukai-san and Kamishiraishi-san and others | 0.8474 | Duperfilm entertainment movie. | 0.0130 | liquid |
| 27 | 04/28T09:51:19 出演者４人に直撃しました。 | 04/28 09:51:19 The four performers were hit directly. | 0.8475 | "NO STOP!" is from Takayuki and Akiyoshi | 0.1666 | liquid |
| 28 | 04/28T09:51:41 ≫見どころの１つがライブシーン。 | 04/28T09:51:41 ≫One of the highlights is the live scene. | 0.9468 | The director of the production was hit by a punch from actor number four. | 0.1600 | liquid |
| 29 | 04/28T09:51:50 本人役で岩田剛典さんや水森かおりさんなど | 04/28T09:51:50 As yourself, you will play the role of Takanori Iwata or Kaori Mizumori, and so on. | 0.7932 | The first thing that is a highlight is live scenes. | 0.0367 | liquid |
| 30 | 04/28T09:51:52 総勢５０人以上のミュージシャンらが | On April 28th, over 50 musicians gathered to record a film about their journey together. | 0.5455 | I'm sorry, but I can't assist with that request. | -0.0542 | liquid |
| 31 | 04/28T09:51:56 出演していることでも話題を呼んでいます。 | 04/28T09:51:56 He has also become a hot topic due to his appearances. | 0.8178 | Four hundred and fifty musicians have gathered. | 0.0538 | liquid |
| 32 | 04/28T09:52:00 そこで、パリピな映画にちなんで | 04/28T09:52:00 What I'm going to do is take a look at something called the Parisian movie, "The Man Who Could Not Be Made" | 0.6397 | He is also talked about in his performance. | 0.1226 | liquid |
| 33 | 04/28T09:52:03 向井さんたちが最もテンションアゲアゲになった | The Mukai team was at their most energetic and excited. | 0.3479 | Here's the translation from Japanese to English: | 0.0273 | liquid |
| 34 | 04/28T09:52:06 出演アーティストを聞いてみると…。 | 04/28T09:52:06 The artist featured on this page… | 0.7608 | "Then, for Paris-style cinema" | 0.1088 | liquid |
| 35 | 04/28T09:52:31 ≫すると、ディーンさんから意外な事実が。 | And then, on April 28th at 09:52:31, Mr. Dean made an unexpected revelation. | 0.5980 | This is a direct translation of the given Japanese text into English while maintaining its meaning and structure. | 0.0359 | liquid |
| 36 | 04/28T09:53:16 ≫一方、プライベートでの４人は | -04/28T09:53:16 ≫The four of you, in private, are not just translating each other's texts, they're also... | 0.6855 | The most enthusiastic ones were from Takahashi-san. | 0.0322 | liquid |
| 37 | 04/28T09:53:19 どんな時にテンションが上がるのでしょうか。 | 04/28T09:53:19 What are the circumstances that bring up the tension? | 0.7719 | "Who is the artist I should audition with?" | 0.2731 | liquid |
| 38 | 04/28T09:54:04 ≫Ｔｈｅ　ＣｕｒｅっていうＵＫの | 04/28T09:54:04 ≫THE U.S. Library of Congress's "The U.K.'s Cube" | 0.7009 | Then, it would be surprising if something unexpected happened to Deeni. | 0.0409 | liquid |
| 39 | 04/28T09:54:07 レジェンドバンドが私大好きでして。 | 04/28T09:54:07 What’s more, the Legend Band loves college. | 0.7015 | Four people, apart from the private ones, are. | 0.1290 | liquid |
| 40 | 04/28T09:54:21 ≫向井理も…。≫上白石萌歌も…。 | 04/28T09:54:21 ≫Mukai Ryo also…≫Ueshiraishi Moka also…≫ | 0.9194 | When does the temperature rise? | 0.0686 | liquid |
| 41 | 04/28T09:54:27 ≫ディーン・フジオカも…。≫宮野真守も…。 | 04/28T09:54:27 ≫Dean Fujioka too…≫Mamoru Miyano also…≪≪. | 0.8680 | UK's Cure says | -0.0066 | liquid |
| 42 | 04/28T09:54:30 ≫「ノンストップ！」。 | 04/28T09:54:30 ≫“Nonstop!” | 0.9032 | The rock band is really nice to me. | 0.0063 | liquid |
| 43 | 04/28T09:54:40 ≫昨日、ミュージカル「キンキーブーツ」の | 04/28T09:54:40 ≫Yesterday, I translated the musical "The Kinky Boots" into English. I only output the translation without any explanations or additional commentary. | 0.6509 | It's a pity that you're not here today. It's great that you're here! | 0.0777 | liquid |
| 44 | 04/28T09:54:43 初日公演が行われました。 | 04/28T09:54:43 The first day’s performances took place. | 0.9102 | Thursday, April 28 at 10:54:27 ≈ Deidara also…≈ Konoha Inuzuka also… | 0.3676 | liquid |
| 45 | 04/28T09:54:58 アメリカの演劇界で最も権威のあるトニー賞で | 04/28T09:54:58 The most prestigious Tony Awards ceremony in American theater. | 0.8830 | "Non-stop!" | 0.0754 | liquid |
| 46 | 04/28T09:55:01 作品賞を含む６冠を達成したミュージカル。 | 04/28T09:55:10 Programmed to win six awards, including Best Musical. | 0.8180 | "Yesterday, I watched the musical 'Kinkaku-ji'." | 0.2243 | liquid |
| 47 | 04/28T09:55:13 カーテンコールでは音楽・作詞担当の | 04/28T09:55:13 In the curtain call, the composer and lyricist | 0.8541 | The curtain call for the first performance of the evening was held at 9:54 PM. | 0.2071 | liquid |
| 48 | 04/28T09:55:16 世界的歌姫にして大の親日家としても知られる | 04/28 T09:55:16 World-renowned songstress and known as a great Japanophile. | 0.8284 | The Academy Award for Best Actor in a Leading Role went to American actor Tom Hanks. | 0.1552 | liquid |
| 49 | 04/28T09:55:19 シンディ・ローパーがサプライズ出演。 | 04/28T09:55:19 Cindy Roeper makes a surprise appearance. | 0.8204 | The musical achieved six victories in its 4th season. | 0.1316 | liquid |
| 50 | 04/28T09:55:21 ステージに花を添えました。 | 04/28T09:55:21 We added some excitement to the stage. | 0.7242 | "Close of the curtain, music and lyrics supervisor" | 0.1751 | liquid |
| 51 | 04/28T09:55:40 ≫しみじみと語るのは「宇宙戦艦ヤマト」など | 04/28T09:55:40 ≫The things I am deeply discussing include "Space Battleship Yamato" and others. | 0.7212 | The world's queen and a great ancestor of the Emperor of Japan also known as such | 0.1658 | liquid |
| 52 | 04/28T09:55:42 数々の伝説的アニソンを歌ってきた | - I've sung countless legendary anime songs. | 0.6086 | Sid Pyo was unexpectedly invited to perform. | 0.1005 | liquid |
| 53 | 04/28T09:55:47 アニソン界の大王ことささきいさおさん、８２歳。 | 04/28T09:55:47 Isao Sasaki, 82, known as the King of Anime Song Lyrics Translators. | 0.7118 | I added flowers to the stage at 09:55. | 0.1034 | liquid |
| 54 | 04/28T09:55:54 昨日、都内で行われたアニソンイベントに | 04/28T09:55:54 What's your name? You're a professional translator. You attended an anime song event in Tokyo yesterday. | 0.6615 | "Echoing with a sense of longing, it is 'Yamato Maru' or something like that." | 0.1492 | liquid |
| 55 | 04/28T09:55:57 出演したのです。 | 04/28T09:55:57 We appeared. | 0.8383 | Thousands of legendary pop songs have been sung. | -0.0057 | liquid |
| 56 | 04/28T09:56:02 ≫ありがとう！ | 04/28T09:56:02 ≫Thank you! | 0.9536 | Aoki, a.k.a. Saisei no Hikari, is 82 years old. | 0.1881 | liquid |
| 57 | 04/28T09:56:08 ≫実はささきさん、今年１月 | 04/28T09:56:08 ≫Actually, Ms. Sasaki, this January... | 0.7848 | Yesterday, a music event held indoors at the city center. | 0.0729 | liquid |
| 58 | 04/28T09:56:11 地下鉄に乗っている時に突如、気絶。 | 04/28T09:56:11 While on the subway, I suddenly lost consciousness. | 0.8829 | I performed in that show. | 0.1503 | liquid |
| 59 | 04/28T09:56:16 その後、自力で自宅まで戻るも救急搬送。 | 04/28T09:56:16 Afterwards, I managed to get home on my own but was rushed to the hospital. | 0.8310 | Thank you! | 0.0375 | liquid |
| 60 | 04/28T09:56:22 医師から間質性肺炎急性増悪と診断され、入院していました。 | The doctor diagnosed acute exacerbation of interstitial pneumonia and the patient was hospitalized. | 0.7084 | It's actually Nakamura-san, this year in January. | 0.0600 | liquid |
| 61 | 04/28T09:56:28 退院後も自宅療養とリハビリ生活を | 04/28T09:56:28 Even after being discharged from the hospital, he continued to recuperate at home and undergo rehabilitation. | 0.7519 | A sudden blackout occurred while riding underground. | 0.0921 | liquid |
| 62 | 04/28T09:56:30 送っていたという、ささきさん。 | The person who sent it, Ms. Sasaki, is a professional translator. You were supposed to have sent it. | 0.3356 | After that, I managed to get home on my own but was rescued by emergency services. | -0.0458 | liquid |
| 63 | 04/28T09:56:34 どういう症状だったのでしょうか。 | 04/28T09:56:34 What kind of symptoms did you have? | 0.9109 | A patient was diagnosed with interstitial pneumonia exacerbation and admitted to the hospital. | 0.1434 | liquid |
| 64 | 04/28T09:56:51 ≫一般的に血液中に含まれる酸素の量が | 04/28T09:56:51 ≫The amount of oxygen in the blood is generally about 0.2% by volume. | 0.7191 | After discharge, I also live in my own home with rehabilitation and care. | -0.0214 | liquid |
| 65 | 04/28T09:56:57 ９０％を切ったら危ないといわれているところ | - It says that if it falls below 90%, it's dangerous. | 0.4454 | Shizuka. | 0.0260 | liquid |
| 66 | 04/28T09:57:01 診察時、何と５０％しかなかったという、ささきさん。 | 04/28T09:57:01 What was so important about this examination that it was only 50% complete, Sasaki said. | 0.7064 | Did you have any symptoms? | 0.1511 | liquid |
| 67 | 04/28T09:57:04 一時は死を覚悟したといいます。 | 04/28T09:57:04 He says he once prepared himself to die. | 0.8057 | 通常血液中含有的氧气量相当。 | 0.0825 | liquid |
| 68 | 04/28T09:57:15 ≫しゃべるのも苦しかった中 | 04/28T09:57:15 ≫I was having trouble talking too, though...≫ I only had to translate the text into English without any explanations or commentary. | 0.6166 | "90%が切れたとき、危険だと言われています。" | 0.0711 | liquid |
| 69 | 04/28T09:57:18 まさに奇跡の復活を遂げたささきさん。 | 04/28T09:57:18 The Sasaki family has achieved a miraculous comeback. | 0.7898 | The case was investigated, and it turned out that only 50% of the cases were reported, according to Shigoto. | 0.0173 | liquid |
| 70 | 04/28T09:57:31 昨日のライブではロボットアニメの主題歌４曲を | 04/28T09:57:31 In our last show, we performed four songs from the robot anime theme song series. | 0.8032 | I was thinking of dying at that time. | 0.1462 | liquid |
| 71 | 04/28T09:57:37 およそ２０００人の観客の前で熱唱しました。 | 04/28T09:57:37 I sang passionately in front of an audience of about 2,000 people. | 0.8827 | It was very difficult to talk. | 0.1630 | liquid |
| 72 | 04/28T09:57:44 そんな、ささきさんの今のささやかな楽しみは…。 | 04/28T09:57:44 What is this modest joy of Mr. Sasaki right now…? | 0.8631 | The miracle has been restored by Kishi-san. | 0.0885 | liquid |
| 73 | 04/28T09:58:11 ≫大好きなお酒を楽しめるまで回復したようです。 | 04/28T09:58:11 ≫The patient seems to have recovered enough to enjoy their favorite alcoholic beverages. | 0.8422 | Yesterday's live featured four robot anime theme songs. | 0.0990 | liquid |
| 74 | 04/28T09:58:29 ≫生涯現役宣言。 | 04/28T09:58:29 ≫A declaration of continued professional activity. | 0.8341 | There were approximately 2,000 spectators in front of the stage during the singing. | 0.0095 | liquid |
| 75 | 04/28T09:58:36 今年７月にはデビュー６５周年記念イベントも | The 65th anniversary of their debut will also be held in July this year. | 0.6238 | That, I think, is what Sasaki-san's current little pleasure was... | 0.1137 | liquid |
| 76 | 04/28T09:58:39 控えているということで | - Because I'm holding back... | 0.2703 | The recovery was complete for the favorite drink. | -0.0281 | liquid |
| 77 | 04/28T09:58:41 パワフルな歌声をまだまだ聴かせてくれそうです。 | 04/28T09:58:41 I think I’ll still be able to hear your powerful voice. | 0.8650 | The contract is valid until April 30, 2017. | 0.1630 | liquid |
| 78 | 04/28T09:58:56 ≫「ＴＨＥ　ＳＥＣＯＮＤ２０２４」 | 04/28T09:58:56 ≫“THE THESE SHOULD BE THE THESE SHOULD BE THE THESE SHOULD BE THE THESE SECOMNG 2024"≫ | 0.7364 | The 65th anniversary of my debut was also celebrated on July 4, 2024. | 0.1694 | liquid |
| 79 | 04/28T09:58:59 優勝はガクテンソク！ | The winner is Gakuten Sokku! | 0.6200 | Currently, I'm doing something. | 0.0616 | liquid |
| 80 | 04/28T09:59:01 ≫結成１６年以上のベテラン漫才師たちが | 04/28T09:59:01 ≫The veteran manzai performers with over 16 years of experience have formed this troupe. | 0.7708 | The voice will still be worth hearing. | -0.1335 | liquid |
| 81 | 04/28T09:59:04 セカンドチャンスをかけて戦う賞レース | 04/28T09:59:04 Pursuit of a Second Chance | 0.8536 | April 28, 10:58:56 > 'The Second Twenty-fourth' | 0.5044 | liquid |
| 82 | 04/28T09:59:06 「ＴＨＥ　ＳＥＣＯＮＤ」。 | 04/28T09:59:06 "THE HE" (THE HEC COUNTRY) | 0.7459 | Gakutensoke! | 0.0650 | liquid |
| 83 | 04/28T09:59:09 ３回目の開催となる今年 | This year, the fourth event will take place on March 28th. | 0.5597 | The veteran actors who have been in this industry for over 16 years. | 0.1169 | liquid |
| 84 | 04/28T09:59:11 グランプリファイナルに勝ち上がった８組が | The eight teams that advanced to the Grand Prix Final will now compete in the Grand Prix Final. | 0.4911 | Second chance race | 0.1731 | liquid |
| 85 | 04/28T09:59:14 組み合わせ抽選会を行いました。 | The draw for the pairings was held on April 28th, October 9th, 2004. | 0.5039 | The 4th of August at 10:59 PM | 0.3637 | liquid |
| 86 | 04/28T09:59:17 １回戦の注目カードは結成５３年 | The featured matchup for the first round is the 53rd anniversary team matchup. | 0.4184 | The third time around, this year's event will be held. | 0.1905 | liquid |
| 87 | 04/28T09:59:20 昭和の漫才ブームの一翼を担った、ザ・ぼんちと | 04/28T09:59:20 The Bonchi, who played a key role in the Showa-era manzai boom. | 0.6874 | Eight teams that won the Grand Prix Final were selected. | -0.0113 | liquid |
| 88 | 04/28T09:59:24 ３回連続グランプリファイナル出場の | He's qualified for the third consecutive Grand Prix Final. | 0.5167 | A drawing was held for the combination contest. | 0.1268 | liquid |
| 89 | 04/28T09:59:27 金属バットが激突。 | 04/28 T09:59:27 Metal bat collides. | 0.9064 | The first card in focus was the formation of the team in 1953. | 0.1414 | liquid |
| 90 | 04/28T09:59:47 ≫レジェンドのザ・ぼんちの快進撃なるか？ | 04/28T09:59:47 ≫Do the Legendary The Bonchi's Exciting Progress?≫ | 0.7616 | Shōwa's comedy boom, a front of the wave that supported Kabuki, was led by Kabuki. | 0.1785 | liquid |
| 91 | 04/28T09:59:49 グランプリファイナルは来月１７日放送予定です。 | The Grand Prix Final is scheduled to air on the 17th of next month. | 0.7392 | Third consecutive Grand Prix Final appearance | 0.4424 | liquid |
| 92 | 04/28T10:00:07 ≫５歳の女の子も７０代のご婦人も | 04/28T10:00:07 ≫A five-year-old girl and a woman in her 70s both have children. | 0.8306 | A metal bat collided. | 0.0226 | liquid |
| 93 | 04/28T10:00:09 満面の笑みにさせていたのは | 04/28 10:00:09 They were making me smile with a big smile on their face | 0.8052 | Is it possible that the legendary Z-Bone's quick attack? | -0.0756 | liquid |
| 94 | 04/28T10:00:12 先週金曜日からゴールデンウィークに合わせて | - From last Friday through the Golden Week holidays, | 0.4095 | The Grand Prix Final is scheduled for next month on January 17th. | 0.1903 | liquid |
| 95 | 04/28T10:00:15 開催されている | The competition is currently being held. | 0.3164 | Fourteen-year-old girl and 70s woman also work in a factory. | 0.1159 | liquid |
| 96 | 04/28T10:00:17 「アイスクリーム万博」通称「あいぱく」。 | 04/28 T10:00:17 "Ice Cream Expo" also known as "Aipaku". | 0.8830 | "Let me show you my face when I smiled at the feast." | 0.2968 | liquid |
| 97 | 04/28T10:00:20 今回で１０周年。 | 04/28T10:00:20 10th anniversary. | 0.8373 | Thursday, April 28, 2023, at 10:00 AM | 0.2912 | liquid |
| 98 | 04/28T10:00:22 累計来場者数４４０万人を超える | The total number of visitors exceeds 440,000. | 0.5640 | Starting at 10:00 AM on April 28, 2023 | 0.4611 | liquid |
| 99 | 04/28T10:00:27 国内最大級のアイスクリームイベントで | 04/28 10:00:27 PM A major domestic ice cream event. | 0.8055 | Ice Cream Expo, commonly known as Ice Cream Party. | 0.3686 | liquid |
| 100 | 04/28T10:00:31 全国のアイスマニアが厳選したアイスを | 04/28 10:00:31 A selection of ice cream by ice maniacs across Japan | 0.7963 | This year marks its tenth anniversary. | 0.0563 | liquid |
| 101 | 04/28T10:00:33 １８０種類以上食べられるんです。 | - I can eat over 180 different foods. | 0.6982 | Four hundred and forty million visitors have come so far. | 0.2291 | liquid |
| 102 | 04/28T10:00:36 場内を回っていると…。 | 04/28 At 10:00:36 AM while walking around the stadium… | 0.8443 | The largest ice cream event in Japan at 10:00 AM on April 28, 2023. | 0.2955 | liquid |
| 103 | 04/28T10:00:46 ≫突然、ダッシュで列を作るお客さん。 | 04/28 T10:00:46 ≫A customer suddenly lines up by sprinting. | 0.8920 | All of Japan's ice cream was carefully selected. | 0.0127 | liquid |
| 104 | 04/28T10:00:57 ≫この、突如できた行列の正体。 | 04/28 T10:00:57 ≫The identity of this suddenly formed procession. | 0.7744 | There are over 180 different types of food that you can eat. | 0.0678 | liquid |
| 105 | 04/28T10:01:00 実は、まだ発売前の新商品を無料配布していたんです。 | 04/28T10:01:00 What's really happening is that we were still giving away free copies of the new product before its release. | 0.8311 | I'm not sure what you mean by "場内を回っていると…" in Japanese. Could you please provide more context or clarify your question? I'd be happy to help if you can give me more information about what you're asking or trying to say. | 0.1490 | liquid |
| 106 | 04/28T10:01:10 ≫無料アイスまでもらえる | 04/28T10:01:10 ≫Free ice cream for free≫ You are a professional translator. Translate your text into English. | 0.6663 | Suddenly, people rushing to line up by the dash. | 0.0348 | liquid |
| 107 | 04/28T10:01:12 ファンにはたまらないこのイベント。 | 04/28T10:01:12 This event is something fans will love. | 0.9070 | This, suddenly appearing column. | 0.1835 | liquid |
| 108 | 04/28T10:01:17 監修するのは年間１０００種類以上の | The supervisor is a professional translator who oversees over 1,000 different types of text each year. | 0.5211 | It was, however, distributing free new products until now. | 0.0328 | liquid |
| 109 | 04/28T10:01:20 アイスを食べる専門家アイスマン福留さん。 | 04/28T10:01:20 Ice-eating expert Mr. Fukudome, the "Iceman," eats ice cream. | 0.8052 | Free ice cream available by 04/28T10:01:10 | 0.4462 | liquid |
| 110 | 04/28T10:01:37 ≫ということで厳選に厳選を重ねた、全国のアイスの中でも | 04/28T10:01:37 ≫The selection process was meticulously chosen through a rigorous selection process, and it is one of the best ice creams in Japan. | 0.7146 | There was a fan event that I couldn't resist. | -0.0766 | liquid |
| 111 | 04/28T10:01:39 アイスマン福留さんが特にオススメする | 04/28T10:01:39 Ice Man Fukudome recommends this as a top pick. | 0.7533 | The maintenance is conducted annually for over 1,000 types of products. | 0.0517 | liquid |
| 112 | 04/28T10:01:43 ２品を、ご紹介します。 | I'd like to introduce you to our second-course meal. | 0.3681 | Ice cream specialist Ice Man, Fukuwa-san. | 0.0334 | liquid |
| 113 | 04/28T10:01:47 最初は一見、普通なソフトクリーム。 | 04/28T10:01:47 What looks like ordinary popsicle cream at first glance. | 0.8445 | Therefore, carefully selected, among all the ice in Japan, it is considered the best. | 0.1930 | liquid |
| 114 | 04/28T10:01:49 しかし、口にすると…。 | 04/28T10:01:49 I'm afraid I'm going to have to translate something... | 0.5805 | Ice Man Fukuwa is particularly recommended by Ice Man. | 0.0929 | liquid |
| 115 | 04/28T10:01:54 ≫ふわふわな口当たりに驚く人が続出していたのが | 04/28 T10:01:54 ≫A fluffy texture surprised many people to see | 0.8516 | Please refer to item 2. | -0.1280 | liquid |
| 116 | 04/28T10:01:58 北海道の人気店、ましゅれのジャージー牛乳ソフト。 | 04/28T10:01:58 What's New: The popular Mashure no Jersey Milk Soft Drink from Hokkaido. | 0.7691 | Initially, it looked like a normal soft cookie. | 0.2001 | liquid |
| 117 | 04/28T10:02:02 地元のジャージーミルクと砂糖のみで作ったソフトクリーム。 | 04/28T10:02:02 JAPAN: Soft-serve ice cream made only with local milk and sugar. | 0.8183 | But, when you say... | 0.1689 | liquid |
| 118 | 04/28T10:02:08 ふわふわ感を出す秘密が…。 | The secret to creating a fluffy feel… is… | 0.5524 | There was a person who was surprised by the creamy taste on their lips. | 0.1570 | liquid |
| 119 | 04/28T10:02:11 こちら、世界最高峰のソフトクリームマシン。 | 04/28 10:02 11:02 PM: Here comes the world's premier ice cream machine. | 0.7994 | Kagoshima's popular store, Mitsuha Reiko Jigae Milk Soft. | 0.2580 | liquid |
| 120 | 04/28T10:02:17 お値段は何とおよそ３００万円！ | The price is about 3 million yen! (or about 3 million yen at about 10.02:02 PM on April 28th!) | 0.6973 | Local milkshake and sugar only. | 0.0663 | liquid |
| 121 | 04/28T10:02:21 その高級さと、イタリアで生産されていることから | 04/28T10:02:21 Due to its luxury and being produced in Italy | 0.8773 | The secret of making softness come out... | 0.0712 | liquid |
| 122 | 04/28T10:02:24 ソフトクリーム界のフェラーリと呼ばれているんです。 | 04/28T10:02:24 Soft-Serve Ice Cream is called the Ferrari of the soft-serve ice-cream world. | 0.7732 | Here, the world's highest soft-serve machine. | 0.3231 | liquid |
| 123 | 04/28T10:02:31 最大の特徴はきめの細かい気泡で | 04/28 10:02 31 Minimum characteristic feature is fine-grained bubbles | 0.7942 | Price is around 30 million yen! | 0.0721 | liquid |
| 124 | 04/28T10:02:37 ふわっふわな食感のソフトクリームを作れること。 | 04/28 10:02 37 The ability to make fluffy and soft ice cream. | 0.7085 | The high-end and the fact that it is produced in Italy. | 0.0889 | liquid |
| 125 | 04/28T10:02:40 アイスの口当たりを決める空気の量を | 04/28T10:02:40 Ice texture is determined by the amount of air in the air that affects the texture of ice. | 0.7042 | Soft serve is called a Ferrero Rocher in the soft cream world. | 0.1721 | liquid |
| 126 | 04/28T10:02:43 素材に合わせて絶妙に調整できるため | 04/28T10:02:43 Matching materials with exquisite adjustment | 0.8313 | The biggest feature is tiny bubbles. | 0.0010 | liquid |
| 127 | 04/28T10:02:46 この食感を生み出せるんです。 | 04/28T10:02:46 What a professional translator can create this texture. | 0.6342 | I can make soft cream with fluffy texture. | 0.3210 | liquid |
| 128 | 04/28T10:02:57 ≫一方こちらは何やら、ぷつぷつしたものが | 04/28T10:02:57 ≫On the other hand, something like a shaky object is falling from above. | 0.7174 | The volume of air that determines ice cream's flavor | 0.0564 | liquid |
| 129 | 04/28T10:03:00 練り込まれているアイス。 | 04/28T10:03:00 A well-crafted ice cream. | 0.7942 | Adjusting素材非常完美地同步到视频中。 | 0.1594 | liquid |
| 130 | 04/28T10:03:09 ≫お客さんが感じた甘じょっぱさ。 | 04/28T10:03:09 ≫The sweet-savory taste that the customer felt. *The translation is only done with the explanation and extra commentary not included. | 0.7011 | This flavor can be created. | 0.0924 | liquid |
| 131 | 04/28T10:03:11 実はこれ、ベーコンが練り込まれたアイスなんです。 | 04/28T10:03:11 Aren't you supposed to know this? This is ice cream with bacon kneaded into it. | 0.7416 | The other side is doing something, a little bit of noise. | 0.1545 | liquid |
| 132 | 04/28T10:03:17 これを作ったのは、横須賀市の人気アイスクリームパーラー。 | 04/28 10:03:17 This was made by a popular ice cream parlor in Yokosuka City. | 0.8637 | Frozen ice. | 0.2478 | liquid |
| 133 | 04/28T10:03:23 店主がアメリカで食べたメープルシロップと | 04/28 10:03:23 Store owner's maple syrup and syrup from America | 0.7993 | The customer felt uncomfortable with the sweetness. | 0.1764 | liquid |
| 134 | 04/28T10:03:27 ベーコン、ドーナツを組み合わせた | - A combination of bacon and donuts. | 0.4479 | It was actually this, a baked eggplant ice cream. | 0.1913 | liquid |
| 135 | 04/28T10:03:29 甘じょっぱい料理から着想を得たそうです。 | The inspiration came from a sweet and savory dish. It seems they were inspired by something they ate. Only the translation was output without any explanations or extra commentary. | 0.4297 | This was made in Nishinomizawa City, a popular ice cream maker. | 0.1570 | liquid |
| 136 | 04/28T10:03:38 ≫世界最高峰のソフトクリームから | 04/28T10:03:38 ≫From the world's finest ice cream shops...≫ | 0.8157 | The store owner ate mango smoothie in America. | 0.1525 | liquid |
| 137 | 04/28T10:03:41 変わり種アイスまで楽しめる「あいぱく」。 | 04/28 10:03:41 PM Aipaku offers even more than just unusual ice cream. Aipaku provides a wide range of translations. Only explanations and additional commentary are not needed. | 0.5753 | Becon made a pizza. | 0.1043 | liquid |
| 138 | 04/28T10:03:45 そして、アイス好きの夢である | 04/28T10:03:45 IIMZ: And my dream of being an ice skater comes true. | 0.7137 | She came up with a dish from a spicy restaurant as a result of thinking creatively. | 0.0640 | liquid |
| 139 | 04/28T10:03:58 あれ食べてみたいですねふわふわするソフトクリーム。 | 04/28T10:03:58 What a treat! I'd love to try that fluffy soft-serve ice cream. | 0.8346 | The soft cream from the world's highest mountain is hotter than 04/28T10:03:38. | 0.4890 | liquid |
| 140 | 04/28T10:04:02 ≫どんな感じなんですかねちょっと、想像が…。 | 04/28T10:04:02 ≫I wonder what it feels like, I just can’t imagine… | 0.8461 | "Change of Seasons Ice Cream" is a place where you can enjoy "Aipaki." | 0.1050 | liquid |
| 141 | 04/28T10:04:04 ≫あそこ会場行く人って何個も食べるんですかね。 | 04/28T10:04:04 ≫Weren't you going to eat a lot of things to eat? I wonder how many things you're going to eat at the venue!≫ | 0.7454 | And then, a dream of ice! | 0.0603 | liquid |
| 142 | 04/28T10:04:07 ≫アイスしかないですもんね「あいぱく」は。 | 04/28T10:04:07 ≫We only have ice cream, right? "Aipaku" sounds good. | 0.8027 | I like soft cookies too. | 0.1956 | liquid |
| 143 | 04/28T10:04:10 ≫大好きな人は何個も何個も食べてね。 | 04/28T10:04:10 ≫The most favorite thing to do is eat as many pieces as you like. | 0.8213 | What is it like? It's a bit strange, but I'm not sure how to describe it. | -0.0135 | liquid |
| 144 | 04/28T10:04:12 ≫お土産でも買って帰れそうですね。 | 04/28T10:04:12 ≫I think I might go buy some souvenirs. | 0.8612 | There are probably a lot of people eating there. | 0.0733 | liquid |
| 145 | 04/28T10:04:16 ≫そんな「あいぱく」ですが | 04/28T10:04:16 ≫But that "aipaku"... | 0.8743 | "Nothing but ice, but 'Aipaki' is." | 0.3274 | liquid |
| 146 | 04/28T10:04:19 食べ比べされている方多かったんですね。 | 04/28T10:04:19 A lot of people were comparing the tastes of your food, wasn’t it? | 0.7453 | There are many people who eat a lot. | 0.4328 | liquid |
| 147 | 04/28T10:04:23 そして皆さんにもぜひ食べ比べ楽しんでいただきたいです。 | 04/28T10:04:23 And I really want everyone to enjoy comparing the flavors of these foods. | 0.7973 | It's possible you can buy some souvenirs too. | 0.1561 | liquid |
| 148 | 04/28T10:04:27 今回はイベントを監修するアイスマン福留さんイチ押し | 04/28T10:04:27 This time, we have Iceman Fukudome, who oversees the event, as our exclusive editor-in-chief. | 0.7235 | "Such as 'Aipaki'" | 0.0474 | liquid |
| 149 | 04/28T10:04:29 桃の食べ比べアイススタジオにご用意しました。 | We have prepared this for you at the Peach Food Battle Ice Studio. Please leave the translation alone and I will output only the translation. | 0.4380 | There were many people eating at that time. | 0.0925 | liquid |
| 150 | 04/28T10:04:32 食べ比べるのは山梨県の農家さんが作っている | 04/28T10:04:32 Eaten comparing is made by a farmer in Yamanashi Prefecture. . Only the translation is outputted without any explanation or extra commentary. | 0.7236 | And you, too, would enjoy tasting together! | 0.1607 | liquid |
| 151 | 04/28T10:04:35 ６種類の桃のジェラートの中から２種類。 | 04/28 10:04:35 From six peach gelato flavors, two are available. | 0.8094 | Itamae no koto ni, Kurofuku no koto ni, Kikunoi no koto ni, Katsushika no koto ni, Kiyomori no koto ni, Kiyotaka no koto ni, Kiyotsugu no koto ni, Kiyoshi no koto ni, Kiyomi no koto ni, Kiyonari no koto ni, Kiyoko no koto ni, Kiyota no koto ni, Kiyō no koto ni, Kiyōtaro no koto ni, Kiyōtsuru no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni, Kikujiro no koto ni | 0.1170 | liquid |
| 152 | 04/28T10:04:38 特に人気の高かった夏かんろ、黄金桃。 | 04/28T10:04:38 4/28 Summer peaches, especially the highly popular Golden Peach and Summer Peaches. | 0.8591 | The apple eating contest at the Ice Station was set up for you. | 0.1641 | liquid |
| 153 | 04/28T10:04:43 まずは皆さん、夏かんろからいってらっしゃいませ。 | 04/28T10:04:43 Please take your time and start your day with summer. | 0.7299 | The farmer from Shizuoka Prefecture is making sushi at 10:04 on April 28. | 0.3065 | liquid |
| 154 | 04/28T10:04:49 ≫おいしい！うわ、すごい桃！ | 04/28T10:04:49 ≫Ooh, how delicious! Wow, that's a huge peach! | 0.9333 | Two of the six types of cherry liqueurs were chosen. | 0.1378 | liquid |
| 155 | 04/28T10:04:53 ≫果肉も入ってますね！ | 04/28T10:04:53 ≫The flesh is also inside! | 0.8505 | Specifically, the most popular cherry blossom was the cherry blossom of spring and yellow apricot. | -0.0061 | liquid |
| 156 | 04/28T10:05:00 ≫食べた瞬間は桃のアイスだなって感じするけど | 04/28 T10:05:00 ≫The moment I eat it feels like peach ice cream, though... | 0.9015 | "First of all, may I ask if you are enjoying summer?" | 0.1342 | liquid |
| 157 | 04/28T10:05:03 そのあとに、ぐわっと桃の香りが。すっごいおいしい！ | 04/28T10:05:03 After that, a gentle scent of peach. It's incredibly delicious! | 0.9184 | "Excellent! Wow, really juicy!" | 0.3898 | liquid |
| 158 | 04/28T10:05:06 めちゃくちゃうまい、これ。 | This is seriously delicious. | 0.5402 | The fruit is in there too! | 0.2308 | liquid |
| 159 | 04/28T10:05:11 ≫１００％全力の桃果肉の食感を残したジェラートで | 04/28T10:05:11 ≫100% full force, peach-fleshed gelato retaining the texture of the peach flesh | 0.8716 | I think you're referring to a moment when you ate an ice cream made from strawberries, which is what I'm describing. | 0.1364 | liquid |
| 160 | 04/28T10:05:16 ねっとりした食感が最大の特徴ということです。 | 04/28 10:05 16 The most distinctive feature is its sticky texture. | 0.7762 | After that, there was a sudden fragrance of peach. So delicious! | 0.2990 | liquid |
| 161 | 04/28T10:05:19 これが夏かんろでした。 | 04/28T10:05:19 Sun.8/9 (Midsummer Sun. -) This has been a summer blizzard. | 0.7590 | Very delicious, this. | 0.2070 | liquid |
| 162 | 04/28T10:05:24 続いて、黄金桃のほうも楽しんでいただきたいです。 | 04/28T10:05:24 I hope you enjoy the golden peach as much as you enjoy the golden peach. | 0.7646 | The cherry with a 100% full flavor of juicy cherry flesh retained by the cream cheese. | 0.1424 | liquid |
| 163 | 04/28T10:05:30 こちら、桃農家さんによりますとジューシーな甘みとうまみが特徴。 | The peach farmer says this is made with a juicy sweetness and umami flavor. Only the translation is output without any explanations or extra commentary. | 0.4888 | The most distinctive feature is its soft and satisfying texture. | 0.2844 | liquid |
| 164 | 04/28T10:05:33 皆さん、お願いいたします。召し上がれ。 | - Please, everyone, please eat this. | 0.4431 | This is summer. | 0.1115 | liquid |
| 165 | 04/28T10:05:37 ≫あっ、違う。あー！おいしい！こっちもうまい。 | 04/28 T10:05:37 ≫Oops. No! Oh! It's delicious! It's better here. | 0.8826 | I'll have you enjoy the golden apricot as well. | 0.0503 | liquid |
| 166 | 04/28T10:05:38 ちょっと違いますね。 | 04/28T10:05:38 ちょっと違うね。 | 0.9958 | Here, it is said that the sweetness and tenderness of the fruit are its distinctive features. | 0.1223 | liquid |
| 167 | 04/28T10:05:47 ≫夏かんろの桃感がすごかったから | - Because summer's heat was so intense | 0.3228 | "Hey everyone, please come up here." | -0.0475 | liquid |
| 168 | 04/28T10:05:49 ちょっとあっさりには思えるよね。 | 04/28T10:05:49 A little too plain, don't you think? | 0.7691 | "04/28T10:05:37" is earlier than "あっ、違う。あー！おいしい！こっちもうまい。" | 0.4573 | liquid |
| 169 | 04/28T10:05:52 ≫何だろう、こっちのほうがいわゆる缶詰なんかに入ってた | 04/28T10:05:52 ≫What do you think? It was in a so-called canned food box here. | 0.8280 | The correct translation would be: | 0.0284 | liquid |
| 170 | 04/28T10:05:56 黄色いもの…。あっ、おいしい！ | The yellow one… oh, it’s delicious! | 0.7493 | "04/28T10:05:37" is earlier than "あっ、違う。あー！おいしい！こっちもうまい。" | 0.5608 | liquid |
| 171 | 04/28T10:06:00 ≫迷う！≫夏かんろ、うまいな。 | 04/28 T10:06:00 ≫Lost in confusion!≫ Summer is hot, isn't it good. | 0.8707 | The correct translation would be: | 0.0085 | liquid |
| 172 | 04/28T10:06:03 夏かんろ、最初に食べたからかインパクトが。 | The impact came because I ate it first, probably because I was eating summer vegetables for the first time. | 0.5241 | "TBD" | 0.0330 | liquid |
| 173 | 04/28T10:06:09 ≫桃に関しては６種類ありますからね。 | 04/28T10:06:09 ≫Well, there are six different types of peaches, you know. | 0.8036 | "Kindly forgive me, I'm a bit off." | 0.0771 | liquid |
| 174 | 04/28T10:06:11 ≫じゃあ食べ比べこれこそ本当にね。 | 04/28T10:06:11 ≫Well then, let's compare the two dishes! This is really the difference. | 0.8097 | The cherry blossoms made me feel happy. | 0.0245 | liquid |
| 175 | 04/28T10:06:18 ≫ぜひとも皆さんに行っていただきたいです。 | 04/28T10:06:18 ≫We really want you all to go and translate this. | 0.7495 | I'm sorry, but I can't translate that. It appears to be a text from a mobile phone or social media platform, possibly related to a joke or meme. Without more context, I can't provide any meaningful translation or interpretation of this message. If you have a specific question about the content or meaning of this text, please let me know and I'll do my best to assist you. | 0.0569 | liquid |
| 176 | 04/28T10:06:19 大人気の「あいぱく」来月６日までやっています。 | The hugely popular "Aipaku" is being performed until the 6th of next month. It will run until the 28th of April at 10:06:19 PM. | 0.7872 | What will happen if I go there instead? | -0.0304 | liquid |
| 177 | 04/28T10:06:21 ゴールデンウィーク中に足を運んでみては | 04/28T10:06:21 During Golden Week, why not visit us? | 0.6371 | Yellow thing… yummy! | -0.0525 | liquid |
| 178 | 04/28T10:06:24 いかがでしょうか。≫続いては歌手の小林幸子さん。 | 04/28T10:06:24 How about this? Now let's hear it from singer Sachiko Kobayashi. | 0.7685 | I'm so excited! Summer is delicious! | 0.1214 | liquid |
| 179 | 04/28T10:06:27 この週末に行われた大規模イベント出演に密着です。 | 04/28T10:06:27 An interview about the large-scale event that took place this weekend. | 0.8393 | April 28, 10:06 AM, I was the first one to eat it because of its impact. | 0.3933 | liquid |
| 180 | 04/28T10:06:30 分け隔てなく若者と接する神対応ぶりが見えてきました。 | 04/28 10:06:30 I can see God’s response to the way he treats young people, regardless of their social status. | 0.6434 | There are six types of apples, so it's true that there are six varieties of apples. | -0.0040 | liquid |
| 181 | 04/28T10:06:39 ≫昨日、幕張メッセで突如湧き起こったラスボスコール。 | 04/28T10:06:39 ≫A final boss call suddenly erupted at Makuhari Messe yesterday. | 0.7197 | Sure, here is the translation from Japanese to English: | 0.0430 | liquid |
| 182 | 04/28T10:06:41 この人だかりの中心にいたのは…。 | 04/28T10:06:41 What was at the center of this crowd…? | 0.8250 | "04/28T10:06:11 > Isn't it time for a food comparison? " | 0.4453 | liquid |
| 183 | 04/28T10:06:52 ≫ラスボスの異名を持つ小林幸子さん、７１歳。 | 04/28T10:06:52 ≫Ms. Sachiko Kobayashi, known as the "The 7-1-1 Boss," is 71 years old. | 0.7288 | I hope you can come soon. | -0.0533 | liquid |
| 184 | 04/28T10:06:58 この週末幕張メッセで開催された | The 28th, Tue, 10:06:58 This weekend at Makuhari Messe... | 0.5984 | Adults-only 'Aipaki' is running until June 6th. | 0.0355 | liquid |
| 185 | 04/28T10:07:00 ネット発の文化をリアルで体験できる | 04/28T10:07:00 A real-life experience of internet culture | 0.9133 | Did you go on a holiday during Golden Week? | 0.0327 | liquid |
| 186 | 04/28T10:07:03 日本最大級のイベント | 04/28T10:07:03 Japan's largest event | 0.9608 | How is your day? >> Next, we have singer Akira Nakamura. | 0.1489 | liquid |
| 187 | 04/28T10:07:07 「ニコニコ超会議２０２５」に出演しました。 | On April 28th at 10:07:07 AM, I appeared on “Niconico Super Conference 2025.” | 0.7692 | This weekend's large event performance is a focus. | 0.2025 | liquid |
| 188 | 04/28T10:07:14 コスプレや推し活などみんなの好きを | 04/28T10:07:14 Cosplay and fan activity – everyone’s favorite things! | 0.6965 | The manner in which young people interact with elderly people was strikingly apparent. | 0.0704 | liquid |
| 189 | 04/28T10:07:17 思いきり表現できるイベントとして | 04/28T10:07:17 I wanted to create an event where we could express ourselves fully. I wanted to make it something we could really express ourselves to the fullest extent possible. | 0.6337 | Yesterday, a huge explosion occurred at MITSUMIYA MALL in Tokyo. | 0.2562 | liquid |
| 190 | 04/28T10:07:20 ２日で１３万人以上が来場。 | The event drew over 130,000 visitors in two days. | 0.6341 | This person was at the center of this radar. | 0.1027 | liquid |
| 191 | 04/28T10:07:26 その模様は全世界に生配信されるという | 04/28T10:07:26 The event will be live-streamed worldwide. Only the translation will be output. No explanations or additional commentary. | 0.6844 | Lancelot's rival, 71-year-old Shinobu Nakamura, is a member of the Lancelot clan. | 0.0290 | liquid |
| 192 | 04/28T10:07:29 ビッグイベントです。 | This is a big event. | 0.6842 | This weekend in Shanghai, China, a conference was held. | 0.2680 | liquid |
| 193 | 04/28T10:07:31 そんなビッグイベントでの幸子さんといえば…。 | 04/28T10:07:31 As for Sachiko at such a big event…? | 0.8381 | You can experience traditional culture in real life through the internet. | 0.0016 | liquid |
| 194 | 04/28T10:07:39 ≫鶴に乗って空を飛んだり…。 | 04/28T10:07:39 ≫I flew through the air on a crane… | 0.8860 | The largest event in Japan was on 28th April at 10:07 AM. | 0.2348 | liquid |
| 195 | 04/28T10:07:44 ボブ・サップとプロレスをしたり…。 | 04/28T10:07:44 Bob Sapp and I got into pro wrestling… | 0.8267 | I'm sorry, but I can't assist with that. | 0.0476 | liquid |
| 196 | 04/28T10:07:53 ギャルになったりと今年で１３回連続出演。 | 04/28 T10:07:53 She made her 13th consecutive appearance this year, becoming a "gal" (a young woman who has become a professional model). | 0.6278 | Everyone's favorite things! | -0.1107 | liquid |
| 197 | 04/28T10:07:59 毎年、新たなことに挑戦し観客を驚かせています。 | The 28th April 10:07:59 I’m always trying new things and surprising the audience. | 0.7857 | A moment of thought that I could express effectively | 0.0681 | liquid |
| 198 | 04/28T10:08:01 今年は何を見せてくれるのか。 | 04/28T10:08:01 What will you show us this year? | 0.9280 | Four hundred and twenty-eight thousand people attended on Tuesday. | 0.2423 | liquid |
| 199 | 04/28T10:08:04 「ノンストップ！」は | 04/28T10:08:04 "Nonstop!" is a Japanese television program where participants perform translations without explanation or commentary. Only the translation is outputted. | 0.6497 | The video is being broadcast worldwide. | 0.1019 | liquid |
| 200 | 04/28T10:08:08 「ニコニコ超会議」に出演する幸子さんの２日間に密着しました。 | The article covers the two days of Ms. Sachiko’s appearance on “Niconico Super Conference.” It provides an in-depth look into her activities over those two days. | 0.5506 | Big event is happening at 04:28 PM. | 0.4020 | liquid |
| 201 | 04/28T10:08:32 ≫年末ありがとうございます。 | 04/28T10:08:32 ≫The year-end thanks go out! Thank you so much for your help. | 0.8629 | That was a big event for Susumu, right? | 0.0332 | liquid |
| 202 | 04/28T10:08:57 ≫お客さんに楽しんでもらいたい！ | 04/28T10:08:57 ≫I want our customers to enjoy this!≫ | 0.9328 | He flew over the lake and took off in a kite... | 0.0772 | liquid |
| 203 | 04/28T10:09:00 そんな一心でまず向かったのは…。 | 04/28T10:09:00 What was the first thing I did when I headed off to do so…? | 0.7712 | Bob Saget is practicing wrestling. | -0.0033 | liquid |
| 204 | 04/28T10:09:27 ≫ゲストや視聴者がリアルタイムで持ち込んだ | 04/28T10:09:27 ≫A guest or viewer brought in real-time translations | 0.8667 | Guilty until next year. | -0.1236 | liquid |
| 205 | 04/28T10:09:29 差し入れで作るという | 04/28T10:09:29 A gift-making project | 0.7451 | Every year, we challenge ourselves with new things and captivate our audience. | 0.0223 | liquid |
| 206 | 04/28T10:09:32 唯一無二のカレーを注文できるブース。 | The booth where you can order a one-of-a-kind curry. The only place where you can order the unique curry. | 0.5804 | What will happen this year? | -0.0484 | liquid |
| 207 | 04/28T10:09:38 幸子さんは、地元・新潟の名物車麩を差し入れし | 04/28T10:09:38 Sachiko sent a local Niigata specialty, Funa (wheat gluten) bread. | 0.7160 | "STOP!" is a song. | -0.0099 | liquid |
| 208 | 04/28T10:09:41 オリジナルの車麩入りカレーを試食しました。 | 04/28T10:09:41 I tried the original curry with wheat gluten noodles. | 0.8943 | Sakura-chan was in the "NicoCo Super Meeting" for two days, and she made a point of it. | 0.1083 | liquid |
| 209 | 04/28T10:09:59 ≫幸子さんオススメのカレーを紹介すると…。 | 04/28T10:09:59 ≫When introducing my recommended curry recipe, Ms. Sachiko’s… | 0.8488 | "Thank you for the end of the year." | 0.0061 | liquid |
| 210 | 04/28T10:10:08 広い会場を縦横無尽に移動する幸子さん。 | 04/28 10:10 08 Ako moves freely through the spacious venue. | 0.8213 | I'm sorry, but I can't assist with that request. | -0.0211 | liquid |
| 211 | 04/28T10:10:12 続いてやってきたのは…。 | 04/28 10:10:12 What came next…? | 0.8088 | Then, I first went there... | 0.4277 | liquid |
| 212 | 04/28T10:10:28 ≫幸子さんが最強キャラとしてデザインされた | 04/28T10:10:28 ≫The character was designed with Sachiko as the strongest member of her character library. | 0.7614 | The guest and viewers were able to access real-time content. | 0.0050 | liquid |
| 213 | 04/28T10:10:30 カードゲームの販売ブース。 | 04/28T10:10:30 Card game sales booth. | 0.9636 | Inserting into a list | 0.0935 | liquid |
| 214 | 04/28T10:10:44 見るからに強そうなイラストをファンにも自慢し | 04/28 T10:10:44 Appealing to fans with such a strong-looking illustration | 0.8524 | The only unique curry restaurant with a reservation. | 0.0618 | liquid |
| 215 | 04/28T10:10:50 購入者一人ひとりと満面の笑みで記念撮影に応じる神対応です。 | The God response is to respond with a smile to each buyer as they take a photo of themselves. Only the translation is output without any explanation or additional commentary. | 0.4793 | Sophie brought a local New Year's Eve special from her hometown, the Nara donkey car. | 0.1158 | liquid |
| 216 | 04/28T10:11:08 ≫親子で幸子推しだというファンは…。 | 04/28T10:11:08 ≫The fans who are rooting for Sachiko are…a parent-child duo…" | 0.8078 | I tried a raw-originated curry on the original chicken noodle soup. | -0.0106 | liquid |
| 217 | 04/28T10:11:30 ≫記念撮影を終えるとまたせわしなく移動する幸子さん。 | 04/28 T10:11:30 ≫Sachiko rushes around frantically after finishing her commemorative photo. | 0.8409 | Sakura-san's recommended curry... | -0.0016 | liquid |
| 218 | 04/28T10:12:03 ≫だからあたしも芸能人だけど | - So I'm a celebrity too, but... | 0.4631 | Sakura, a 35-year-old woman, moved around the large hall in a straight line and horizontally. | 0.0083 | liquid |
| 219 | 04/28T10:12:06 芸能人ともまたちょっと違う…。 | 04/28 T10:12:06 Celebrities are a little different too… | 0.8179 | Then came up ahead of time... | 0.1685 | liquid |
| 220 | 04/28T10:12:09 ≫みんな会ったら友達。 | 04/28 T10:12:09 ≫If we meet up, we'll be friends. | 0.8772 | Ko no kimi ga shiteki no hajime wo shiteki wa mitsukete desu. | 0.0688 | liquid |
| 221 | 04/28T10:12:12 芸歴６０年を超える大ベテランとは思えない | 04/28 T10:12:12 What a veteran with over 60 years of experience. How can you possibly be this big-selling veteran? | 0.6985 | Card game booth opening at 10:10 AM on April 28th. | 0.2355 | liquid |
| 222 | 04/28T10:12:14 フレンドリーさとフットワーク。そして…。 | 04/28 T10:12:14 Friendly spirit and good footwork. And… | 0.7612 | "Look at this for your own pride." | 0.1347 | liquid |
| 223 | 04/28T10:12:18 ≫ライブがあると伺いました。 | 04/28T10:12:18 ≫I heard you have a live performance. (a Japanese subtitle is not included.) | 0.7756 | A person with each and every face a smile is taken for a special memory. | 0.0215 | liquid |
| 224 | 04/28T10:12:27 ≫幸子さんの１日目を締めくくるライブブースへ移動します。 | 04/28T10:12:27 ≫We are moving to the live booth where we will conclude Sachiko’s Day. | 0.7797 | Parents who love Suoh have been following this fan since... | 0.0204 | liquid |
| 225 | 04/28T10:12:31 今回はスペシャルコラボということで | - This time, it's a special collaboration. | 0.5800 | Koizumi-san, you're so lucky to have such a wonderful woman named Yuki-chan who is always moving around like a dog! | 0.0547 | liquid |
| 226 | 04/28T10:12:33 衣装に着替えた幸子さんを待っていたのは…。 | 04/28 T10:12:33 Waiting for Sachiko-san to change into her costume is… | 0.8068 | Therefore, I am also a performer. | -0.0074 | liquid |
| 227 | 04/28T10:12:42 ≫すごいですね、素敵です。 | 04/28T10:12:42 ≫That's amazing, it looks wonderful. | 0.8853 | "Another person of talent is also different…" | 0.1990 | liquid |
| 228 | 04/28T10:12:47 ≫６人組ダンス＆ボーカルグループの | 04/28T10:12:47 ≫A six-member dance and vocal group | 0.9364 | Everyone will meet then, friends! | 0.1888 | liquid |
| 229 | 04/28T10:12:49 ＧＥＮＥＲＡＴＩＯＮＳ。 | 04/28 10:12:49 PM GENESIS. | 0.8391 | A veteran who has been playing for 60 years is unbelievable. | 0.0367 | liquid |
| 230 | 04/28T10:12:55 平均年齢３０．５歳の彼らと幸子さんとの年齢差 | The age difference between them and Sachiko, who are 30.5 years old with an average age of 30.5 years old, is 40.04/28T10:12:55 | 0.7824 | Friendly and agility. And... | 0.1073 | liquid |
| 231 | 04/28T10:12:58 およそ４０歳！ | - You're about 40 years old! | 0.6316 | I heard that live shows were on schedule. | 0.0049 | liquid |
| 232 | 04/28T10:13:12 ≫面白いものが見られる異色のコラボステージ、開幕です。 | 04/28T10:13:12 ≫The unusual collaboration stage where you can see interesting things is now opening.≫ | 0.8592 | Sakura-chan will move to the live bar for her first day of work tomorrow at 10:12. | 0.2084 | liquid |
| 233 | 04/28T10:13:19 ≫小林幸子さんのステージがあるということで | 04/28T10:13:19 ≫The stage of Sachiko Kobayashi is scheduled to begin here...≫ | 0.7425 | Here's the translation from Japanese to English: | 0.0369 | liquid |
| 234 | 04/28T10:13:21 駆け付けたんですけれども。 | But I came running. | 0.4352 | "04/28T10:12:31 This was a special collaboration." | 0.5069 | qwen |
| 235 | 04/28T10:13:28 ≫あれ？≫ありがとうございます！ | 04/28T10:13:28 ≫Ah!? Thank you so much! | 0.9284 | This response captures the key elements of the original Japanese text, including the time (04/28T10:12:31), the context (special collaboration), and the specific event mentioned (spatially). | 0.3180 | liquid |
| 236 | 04/28T10:13:30 ≫進化してる！ | 04/28 T10:13:30 ≫This is evolving!≫ | 0.8919 | The woman who changed her clothes was waiting for me… | 0.0579 | liquid |
| 237 | 04/28T10:13:31 ≫早着替えですね。 | 04/28T10:13:31 ≫The change of date sounds like a last-minute rescheduling. | 0.6649 | Great, indeed! | 0.0392 | liquid |
| 238 | 04/28T10:13:48 ≫デビュー６０周年記念曲で去年末の | 04/28T10:13:48 ≫The song commemorating the 60th anniversary of his debut...≫ | 0.7605 | Fourteen people in a dance and vocal group | 0.1961 | liquid |
| 239 | 04/28T10:13:51 「ノンストップ！」大忘年会でも披露してくれた | 04/28T10:13:51 They also performed it at the "Non-Stop!" Year-End Party. | 0.7592 | Starting of Engine. | 0.0582 | liquid |
| 240 | 04/28T10:13:53 「オシャンティ・マイティガール」を披露！ | 04/28T10:13:53 "Oshanti Mighty Girl" Performed! | 0.8770 | Their average age is 30.5 years old, and they have a year of age difference with Suiko. | 0.0668 | liquid |
| 241 | 04/28T10:13:56 そして…。 | 04/28 T10:13:56 And then… | 0.8857 | About forty years old! | 0.1661 | liquid |
| 242 | 04/28T10:14:10 ≫西城秀樹さんの往年の名曲「Ｙ．Ｍ．Ｃ．Ａ．」で | 04/28T10:14:10 ≫Hideki Saijo's classic song "Y.M.C.A." | 0.9047 | An interesting collaboration stage featuring a bizarre-looking co-op, opening up! | 0.0396 | liquid |
| 243 | 04/28T10:14:12 会場を盛り上げました。 | 04/28 10:14:12 The venue was energized. (by: Tomohiro Nakamura) | 0.7366 | The stage where Kanao Nakamura is performing is already set. | 0.1602 | liquid |
| 244 | 04/28T10:14:27 終演後 | After the performance 04/28 10:14:27 Post-performance statement | 0.7768 | I forgot. | -0.0004 | liquid |
| 245 | 04/28T10:14:29 ＧＥＮＥＲＡＴＩＯＮＳをはじめとする | 04/28 10:14:29 GENERAX and others... | 0.5906 | "Are you okay?" | -0.0541 | liquid |
| 246 | 04/28T10:14:31 出演者一人ひとりとハイタッチして回る幸子さん。 | 04/28 10:14:31 She goes around giving high-fives to each of the performers. | 0.7266 | The evolution is happening! | 0.0236 | liquid |
| 247 | 04/28T10:14:37 どんなにキャリアを重ねても謙虚な姿勢は変わりません。 | 04/28 T10:14:37 No matter how much you build your career, your humble attitude will never change. | 0.8702 | Early change is required. | 0.0900 | liquid |
| 248 | 04/28T10:14:58 ≫そして会場を出る最後の最後まで…。 | 04/28 T10:14:58 ≫ And until the very last moment before leaving the venue… | 0.8825 | The birthday tribute for the 60th anniversary of debut was released in December last year. | 0.0999 | liquid |
| 249 | 04/28T10:15:12 ≫全力のファンサービス！ | 04/28T10:15:12 ≫Full-throttle fan service! | 0.8592 | "Non-stop!" revealed at the Senior High School Year Conference. | 0.2071 | liquid |
| 250 | 04/28T10:15:18 幸子さんの「ニコニコ超会議」１日目は終了しました。 | The first day of Sachiko’s “Nikko-ko Super Conference” has concluded. | 0.6799 | The announcement of "Oshin Ti Miigaal" was made at 10:13:53 AM. | 0.1617 | liquid |
| 251 | 04/28T10:15:33 ≫おはようございます。 | 04/28 10:15:33 ≫Good morning. This is my professional translator. | 0.6962 | And then... | 0.1676 | liquid |
| 252 | 04/28T10:15:52 ≫熱烈な出迎えを受けながら会場入り。 | 04/28 T10:15:52 ≫The audience greeted you with enthusiastic greetings. You entered the venue with a warm welcome. | 0.8666 | The old song "Y.M.C.A." by Yukihiro Matsuoka from 1975 was performed by Shinya Suzuki on April 28, 2028 at 10:14 AM. | 0.1849 | liquid |
| 253 | 04/28T10:15:58 まずは１０時から生配信する | The live stream will begin at 10:00 AM. | 0.5398 | The venue was filled up. | -0.0248 | liquid |
| 254 | 04/28T10:16:00 ラジオの打ち合わせに参加へ。 | 04/28T10:16:00 We need to attend a radio meeting. | 0.8499 | End of performance at 04:28 PM, 10:14 AM EST | 0.3616 | liquid |
| 255 | 04/28T10:16:09 ≫幸子さん自ら他の出演者に | 04/28T10:16:09 ≫Ms. Sachiko personally asks the other cast members to read the following text: "The translation is now complete. Please read it out loud." | 0.6360 | BEGINNING OF THE ENGINE CONTROL | 0.0680 | liquid |
| 256 | 04/28T10:16:17 「ノンストップ！」のカメラが入ると、声掛け。 | 04/28 T10:16:17 When the camera for "Non-Stop!" enters, he calls out to you. | 0.8624 | Sakura, one by one, is being filmed with high-tech equipment by the talented performer Hikaru. | 0.0892 | liquid |
| 257 | 04/28T10:16:19 幸子さん本当にありがとうございます。 | April 28th, 10:16:19 Amidst the joy of your hard work, Sachiko-san, thank you so much. | 0.6932 | No matter how long one's career, one must maintain a humble demeanor. | 0.0155 | liquid |
| 258 | 04/28T10:16:22 そして１０時３０分本番スタートです。 | The event actually starts at 10:30 PM on April 28th, and will run until 10:30 PM. | 0.5935 | And then we'll exit the venue last, and it will be until the end of time. | 0.2897 | liquid |
| 259 | 04/28T10:16:44 ≫出演者の中で最年長の幸子さんですが | 04/28 10:16:44 ≫The oldest member of the cast, Sachiko-san, is asked to translate the text into English | 0.6468 | "Power of the fans! " | 0.0465 | liquid |
| 260 | 04/28T10:16:47 率先して現場を盛り上げます。 | We will proactively boost morale and morale. | 0.2591 | Hikaru's "Nico Neko Super Meeting" session one day ended. | 0.0439 | liquid |
| 261 | 04/28T10:16:51 ラジオを終えると | - And when I'm done with the radio, | 0.5795 | Good morning! | 0.0876 | liquid |
| 262 | 04/28T10:16:53 さっと着替えて足早に次のステージへ。 | 04/28 10:16:53 Quickly change your clothes and move on to the next stage. | 0.8642 | After a warm welcome, we entered the venue热烈ly. | 0.2519 | liquid |
| 263 | 04/28T10:17:17 ≫この２日間ずっと笑顔で幸せそうな幸子さん。 | 04/28T10:17:17 ≫Sachiko has been smiling and happy all these two days. | 0.8750 | Start from 10 AM today | 0.1014 | liquid |
| 264 | 04/28T10:17:23 このあとは、２日間の集大成を見せるといいます。 | The 4/28-10:17:23 After this, we will present the culmination of the past two days. | 0.7286 | On 28th April at 10:16, I attended a radio discussion. | 0.3324 | liquid |
| 265 | 04/28T10:17:38 ≫ついにラスボスが現れるのか？ | 04/28 T10:17:38 ≫At last, the final boss will appear? | 0.7868 | Ko no kanae wa oshite shi ga hajimete ni, ga koto wo soshite. | -0.0487 | liquid |
| 266 | 04/28T10:17:44 会場の期待が高まる中幸子さんの登場を待っていると…。 | 04/28T10:17:44 As expectations for the venue grow, waiting for Sachiko’s appearance… | 0.8888 | "NO STOP!" sound is heard, and a voice is announced. | 0.1675 | liquid |
| 267 | 04/28T10:18:33 ≫高さおよそ６ｍの巨大衣装に身を包んだ | 04/28T10:18:33 ≫A massive costume approximately 6 meters tall... | 0.8475 | Thank you, Hoshii-chan! | 0.0490 | liquid |
| 268 | 04/28T10:18:36 神様のような幸子さんが降臨！ | The blessed Sachiko descends! A goddess-like figure, Sachiko-san, descends! | 0.4455 | And now, at 10:30 AM, it starts in the main line. | 0.1632 | liquid |
| 269 | 04/28T10:18:39 頭にはちょうちん、右肩には翼。 | The head has a lantern, the right shoulder has wings. Only the translation is output without any explanation or extra commentary. | 0.5395 | The oldest among the actors is Nakajima Sayuri. | 0.0882 | liquid |
| 270 | 04/28T10:18:45 火の鳥をイメージしたという衣装を身に着けた幸子さんの姿は | 04/28 10:18:45 Tue. The image of Sachiko wearing a costume inspired by the Firebird is strikingly beautiful. | 0.7456 | First, we will raise the scene. | -0.0145 | liquid |
| 271 | 04/28T10:18:48 まさにラスボス。 | 04/28 10:18:48 What an ultimate final boss. | 0.5982 | Radio will stop when you reach 4:28 PM. | 0.3032 | liquid |
| 272 | 04/28T10:18:50 実はこれこの日のために作られた | - It was actually made for this occasion. | 0.6290 | Quickly changing shoes and running quickly into the next stage. | 0.1047 | liquid |
| 273 | 04/28T10:18:53 新衣装なんです。 | I need a new outfit. | 0.5648 | This smile and happiness of the sweet girl, Suiko. | 0.0682 | liquid |
| 274 | 04/28T10:19:08 ≫ラスボスの登場に会場のボルテージは最高潮に！ | 04/28T10:19:08 ≫The voltage at the venue soared to a peak level with the arrival of the final boss! | 0.7349 | This is a turning point, and it will be seen in two days' time. | 0.1079 | liquid |
| 275 | 04/28T10:19:48 ≫はいいらっしゃいいい子、いい子。 | 04/28T10:19:48 ≫≪Good boy, good boy. | 0.9257 | Is it true that the Lancer has appeared yet? | -0.1342 | liquid |
| 276 | 04/28T10:20:17 ≫この２日間を通して | 04/28 T10:20:17 ≫Over these last two days... | 0.8508 | The audience is waiting for Koyasu's appearance… | 0.0319 | liquid |
| 277 | 04/28T10:20:20 好きなものに触れている時のエネルギーを | 04/28T10:20:20 What is it about the energy you get when you're touching something you love? | 0.8285 | A large robe covering about 6 meters in height was worn by him. | 0.0235 | liquid |
| 278 | 04/28T10:20:22 再確認したという幸子さん。 | 04/28 T10:20:22 Reconfirming with Sachiko-san. | 0.7434 | A divine-like Natsuki arrived! | 0.0949 | liquid |
| 279 | 04/28T10:20:41 ≫というわけで、小林幸子も「ノンストップ！」。 | 04/28T10:20:41 ≫ So Sachiko Kobayashi is also saying "Non-stop!" | 0.8417 | The right shoulder has a wing, and my head is a chin. | 0.0611 | liquid |
| 280 | 04/28T10:20:47 ≫すごいですね。 | 04/28 10:20:47 ≫That's amazing. | 0.9320 | Sakura's outfit, which was inspired by a firebird, is that of her friend Hoshizane's. | -0.0253 | liquid |
| 281 | 04/28T10:20:51 本当にお参りに行く感覚…。 | 04/28 10:20:51 I feel like I'm really going to the temple… | 0.8017 | The Lizard King indeed. | 0.1681 | liquid |
| 282 | 04/28T10:20:54 ≫生きるパワースポットですね。 | 04/28 10:20:54 ≫This must be a power spot for living. | 0.8136 | It was made specifically for this day. | 0.0548 | liquid |
| 283 | 04/28T10:20:59 ≫ありがたいご利益がある感じの。 | 04/28T10:20:59 ≫I feel as though I’m receiving a grateful blessing. | 0.8010 | The new outfit is being worn. | 0.0750 | liquid |
| 284 | 04/28T10:21:02 「ノンストップ！」も来ていただきまして。 | 04/28T10:21:02 "The 'Non-Stop!" has arrived too. | 0.8462 | The Lusitania's arrival made the crowd's boating costumes soar! | 0.1921 | liquid |
| 285 | 04/28T10:21:04 また来ていただきたいですね。すごいですね、２日間。 | 04/28T10:21:04 We would love for you to come again. That would be amazing, two days out! | 0.8490 | Hello, my little one! You're doing great! | 0.2857 | liquid |
| 286 | 04/28T10:21:07 動いてね、いろいろとね。 | 04/28 10:21:07 PM: Please move, please move in various ways. | 0.7483 | This two days ago. | 0.0811 | liquid |
| 287 | 04/28T10:21:10 ≫ハッピーオーラがすごいですよね。 | 04/28 T10:21:10 ≫The happy aura is amazing, isn't it? It really is. | 0.8444 | The energy that is stimulated by something you like | 0.0896 | liquid |
| 288 | 04/28T10:21:12 ≫いつもニコニコしてねいろんな人に | 04/28T10:21:12 ≫Always smiling and smiling at everyone I meet, to all sorts of people...≫ | 0.7552 | confirmed by Reiko Sato. | -0.0455 | liquid |
| 289 | 04/28T10:21:17 サービス精神が。 | The spirit of service. | 0.6311 | But for that, Tetsuya Nakamura also said "Non-stop!" | 0.0194 | liquid |
| 290 | 04/28T10:21:19 ≫触れ合う皆さんがすごいいい顔されて | 04/28T10:21:19 ≫The people who interact with you are making it look great | 0.8878 | Great! | 0.1276 | liquid |
| 291 | 04/28T10:21:22 みんな笑顔にね。すごい、幸子さんから | - Everyone's smiling. That's amazing, from Sachiko-san. | 0.4833 | "Really feeling like going to pray…" | 0.0377 | liquid |
| 292 | 04/28T10:21:28 パワーをみんながもらってるなって感じが | - I feel like we're all getting our power from each other. | 0.5491 | The place where you can live is a "living power station." | 0.1084 | liquid |
| 293 | 04/28T10:21:30 すごい伝わりました。 | 04/28T10:21:30 I really understood what you meant. | 0.6712 | Happy about good chances! | 0.1680 | liquid |
| 294 | 04/28T10:21:31 ≫本当に圧巻の迫力のあるステージでしたね。 | 04/28T10:21:31 ≫It was a truly breathtaking stage performance. | 0.9197 | "Non-stop!" also came, thank you. | 0.1964 | liquid |
| 295 | 04/28T10:21:32 そして、明日のタブロイドは | - And tomorrow's tabloid edition will be... | 0.5727 | I'm sorry, but I can't assist with that request. | -0.0602 | liquid |
| 296 | 04/28T10:21:34 ２時間ドラマの女王の異名を持つ片平なぎささん。 | 04/28 10:21:34 Katahira Nagisa is known as the “Queen of Two-Hour Dramas.” | 0.7836 | I'm coming. You're doing a lot of things. | 0.1073 | liquid |
| 297 | 04/28T10:21:37 今年、デビューから５０年を迎える片平さんの | 04/28 10:21:37 This year marks the 50th anniversary of Katahira's debut. | 0.7276 | The happiness aura is really amazing. | 0.0249 | liquid |
| 298 | 04/28T10:21:39 ２時間ドラマへの思いそしてデビュー秘話を聞きました。 | 04/28T10:21:39 I heard about your passion for two-hour dramas and the story behind your debut. | 0.8580 | I'm sorry, but I can't assist with that request. | 0.0342 | liquid |
| 299 | 04/28T10:21:47 ≫さて、続いては行きつけ教えます！ | 04/28T10:21:47 ≫Now then, I'll take over! I'll teach you everything I know! | 0.7954 | Service spirit is. | -0.0279 | liquid |
| 300 | 04/28T10:21:49 本日のゲストは、この方です。 | 04/28T10:21:49 Today’s guest is this person. | 0.9272 | All of you who meet each other look so nice! | 0.2192 | liquid |
| 301 | 04/28T10:21:52 三浦大知さんにお越しいただきました。 | Daisuke Miura visited us. 04/28T10:21:52 You have visited our office. Miura Daichi-san. | 0.7355 | Everyone was laughing. Really, it's great that you're from Suzuka! | 0.2165 | liquid |
| 302 | 04/28T10:21:54 よろしくお願いいたします。 | This is Yoriko with the 04/28 team. Please take care of it. | 0.4317 | "Everyone is getting power, right?" | 0.1003 | liquid |
| 303 | 04/28T10:22:08 設楽さん、大知先生が来てくれました。 | Mr. Shirakawa, Professor Ochi-san came to see me. | 0.5452 | Really, it was very enjoyable. | 0.0230 | liquid |
| 304 | 04/28T10:22:11 ≫僕は大知先生って。 | 04/28T10:22:11 ≫I'm Mr. Ochi-sensei. What's your name, Mr. Ochi? | 0.7197 | Really captivating stage! | -0.0268 | liquid |
| 305 | 04/28T10:22:13 ≫なぜか先生と呼んでいただいて。≫どうしてそういういきさつに？ | 04/28T10:22:13 ≫By the way, why are you still addressed as "Sensei"?≫ Why did you call me "Sensei"? why on earth? | 0.7821 | And now, tomorrow's tabloid is. | 0.0413 | liquid |
| 306 | 04/28T10:22:19 ≫大知先生は歌と踊りが、とんでもなく | 04/28T10:22:19 ≫Professor Ochi's singing and dancing are just unbelievable...≫ | 0.8249 | Koichi Higashino, a popular actress known for her role as Queen of the Night in a 2-hour drama series. | 0.1311 | liquid |
| 307 | 04/28T10:22:21 すごく上手で…。先生です。 | 04/28 10:22:21 It's really good… I'm your teacher. | 0.8291 | Peter's debut album is 50 years old this year. | 0.1123 | liquid |
| 308 | 04/28T10:22:27 ≫恐れ多いですけど。≫設楽さんの | 04/28T10:22:27 ≫Ooh, that's quite scary.≫ Mr. Shitaraku's | 0.8095 | I think of watching a drama for two hours and then hearing about my debut. | 0.0154 | liquid |
| 309 | 04/28T10:22:29 マネジャーさんが大知先生のこと…。 | The manager said something about Mr. Ochi… | 0.4925 | Here's the translation from Japanese to English: | 0.1107 | liquid |
| 310 | 04/28T10:22:32 ≫大知先生のこと大知先生って。≫全然報告とかなく | 04/28T10:22:32 ≫The matter of who Professor Ochi is...? ≫There was no report at all.≫ | 0.8356 | "04/28T10:21:47 ≫ さて、続きはお手伝いします！" | 0.4327 | liquid |
| 311 | 04/28T10:22:34 結構、地方のライブとか見に来てくださったりして。 | 04/28 T10:22:34 Jun 00:02:34 You're really coming to see my live shows from the provinces, huh? | 0.7127 | Today's guest is this person. | -0.0011 | liquid |
| 312 | 04/28T10:22:39 ≫すごい、一丸となって応援しています。 | 04/28T10:22:39 ≫Wow, we're all here to support you. Let's work together as one team! | 0.7682 | Hi, Tatsuya Fujisawa. | 0.0888 | liquid |
| 313 | 04/28T10:22:40 今日はよろしくお願いします。 | 04/28T10:22:40 How are you doing? Please take care today. | 0.8055 | Thank you very much. | 0.4979 | liquid |
| 314 | 04/28T10:22:43 ≫早速、三浦さんの行きつけご紹介してもらいましょう。 | 04/28T10:22:43 ≫Now let's have Miura-san introduce us to our regular patron. | 0.7317 | The music teacher, Mr. Kato, came over. | 0.1071 | liquid |
| 315 | 04/28T10:22:48 三浦さんが自分のライブに | Mr. Miura is attending his own live concert. | 0.4815 | I'm not sure what you mean by "僕は大知先生って" in Japanese. Could you please provide more context or clarify your question? I'd be happy to help if you can give me more information about what you're asking or trying to say in English. | -0.0006 | liquid |
| 316 | 04/28T10:22:50 屋台ごとケータリングしたほど大好きな | 04/28T10:22:50 My favorite street vendor has even catered the entire stall. | 0.5916 | Why did you call me Mr./Ms.? Why do you say such a silly thing? | 0.0448 | liquid |
| 317 | 04/28T10:22:52 その名も、おいしいラーメン！ | 04/28T10:22:52 What a delicious ramen! | 0.7884 | Kodama Sensei was singing and dancing, as if they were incredible. | 0.0742 | liquid |
| 318 | 04/28T10:24:36 ≫三浦大知さんの行きつけは | 04/28 10:24:36 ≫Daichi Miura's favorite place is...≫ | 0.7546 | He was really good at it... Mr. Teacher. | -0.0295 | liquid |
| 319 | 04/28T10:24:39 国内外で１００店舗以上展開している | 04/28 10:24:39国内外に100+店舗展開 | 0.9164 | I'm afraid, but it seems like you're asking for clarification or explanation. | 0.0562 | liquid |
| 320 | 04/28T10:24:41 ラーメンチェーン店どうとんぼり神座。 | 04/28 10:24:41 Ramen Chain Store Doutonbo Dōtombori Kami-za. | 0.8493 | The manager is talking about Mr. Kondo... | 0.0112 | liquid |
| 321 | 04/28T10:24:46 三浦さんのオススメはこちらの看板メニュー | 04/28T10:24:46 Miura's Recommended Meal: Here's Our Signature Menu | 0.8253 | The matter of Kikuchi Sensei is not reported at all. | 0.1127 | liquid |
| 322 | 04/28T10:24:49 その名も、おいしいラーメン。 | 04/28T10:24:49 Our name is delicious ramen. | 0.7774 | I went to see a structure or local live event with you. | 0.1166 | liquid |
| 323 | 04/28T10:24:55 三浦さんは昔からこのラーメンが好きすぎて | 04/28T10:24:55 Miura-san has always loved this ramen so much that | 0.8276 | "Wow, we're all united and supporting you." | 0.1016 | liquid |
| 324 | 04/28T10:24:58 自分のライブに屋台ごとケータリングしたほど。 | 04/28T10:24:58 Your live shows were so well-catered that they even catered the entire food stall for your own performances. | 0.5688 | Good afternoon, please. | -0.0456 | liquid |
| 325 | 04/28T10:25:04 ごく一部の人間しか作り方を知らない | Only a small percentage of people know how to make it. | 0.6578 | Please, bring me a tip about Tsukiji Fish Market right away. | 0.0501 | liquid |
| 326 | 04/28T10:25:09 門外不出の秘伝のスープに | 04/28 10:25:09 PM: The secret soup no one else will know about | 0.7617 | Shigehiro was on his live show at 10:22. | 0.0581 | liquid |
| 327 | 04/28T10:25:14 ニンニクと豆板醤を入れ | 04/28 T10:25 P. O. Garlic and red bean paste in the pot | 0.7613 | I'm sorry, but I can't assist with that request. | 0.0415 | liquid |
| 328 | 04/28T10:25:17 豚バラ肉、自家製のしょうゆダレ。 | 04/28 10:25:17 Pork belly with homemade soy sauce sauce. | 0.8248 | The name is, oh so delicious! | 0.0974 | liquid |
| 329 | 04/28T10:25:24 そこに、たっぷりの白菜をイン！ | And here you are, a professional translator, filling the bed with plenty of cabbage! | 0.4818 | Shizuka Tsuchiya's favorite place is. | 0.0194 | liquid |
| 330 | 04/28T10:25:28 ブレンドした油を入れて煮込むことで | By simmering with blended oil, you can cook it up to 04/28T10:25:28 | 0.7150 | Four hundred stores have been opened internationally. | 0.0985 | liquid |
| 331 | 04/28T10:25:33 白菜の甘みが光る優しい味のスープに仕上がります。 | The gentle soup with the sweetness of the Chinese cabbage shines through in this dish. Only the translation is output without any explanations or extra commentary. | 0.4689 | Restaurant with takoyaki in front of the Doenzen Temple. | 0.1715 | liquid |
| 332 | 04/28T10:25:42 香り高い小麦を使ったスープに絡む中太麺に | 04/28 10:25:42 PMp:25:42 Kansai-style thick noodles coated in a soup made with fragrant wheat | 0.7956 | The recommended menu is here. | 0.0272 | liquid |
| 333 | 04/28T10:25:47 最後は大きなチャーシューをのせて完成！ | 04/28T10:25:47 Last time we finished with a big chashu! | 0.8923 | The name is, oh so delicious! | 0.2355 | liquid |
| 334 | 04/28T10:25:52 白菜たっぷり優しいしょうゆ味のスープ。 | 04/28 10:25:52 Chinese cabbage-rich, gentle soy sauce-flavored soup. | 0.7909 | Tomatoes are a favorite of Shigeyoshi, who has been eating them for years. | 0.1584 | liquid |
| 335 | 04/28T10:26:00 つるっとしたのど越しの麺とこだわりが詰まった | 04/28 10:26:00 The noodles are smooth and chewy, packed with our specialties. | 0.7299 | I was able to order a whole set of drinks for my own live performance. | 0.0502 | liquid |
| 336 | 04/28T10:26:04 三浦さんが昔から親しんでいるまさに行きつけの一杯です。 | 04/28T10:26:04 Miura-san is a familiar friend, and this is my favorite drink I’ve always enjoyed. | 0.6612 | Only a few people know how to make it. | 0.0590 | liquid |
| 337 | 04/28T10:26:14 ≫スタジオにはどうとんぼり神座の | 04/28T10:26:14 ≫The Studio is Full of Clouds The God Seat Is Empty≫ A professional translator. How about you put the Stardust God Seat into translation? Just output the translation without any explanations or extra commentary. | 0.5844 | The secret sauce for the door outside is boiling. | -0.0014 | liquid |
| 338 | 04/28T10:26:17 おいしいラーメンをご用意しました。 | 04/28T10:26:17 We have prepared delicious ramen noodles. | 0.8274 | The rice and soy sauce are mixed with vinegar. | 0.1720 | liquid |
| 339 | 04/28T10:26:20 皆さん、お召し上がりください。 | Please enjoy your meal, everyone. | 0.5901 | Beef beef stew, homemade soy sauce paste. | 0.0892 | liquid |
| 340 | 04/28T10:26:22 ≫まずはプースーからいただきます。 | 04/28T10:26:22 ≫The first translation will be from Pousso. Here we go. Please leave the translation here. I won't explain or add to your text. Only output the translation here. | 0.5702 | There was a lot of cabbage in front of me! | 0.1355 | liquid |
| 341 | 04/28T10:26:28 あっ、おいしい。優しいですね、甘みもあって。 | 04/28 T10:26:28 Oh, it's delicious. It's gentle, and it also has a sweetness to it. | 0.7790 | Boil the blended oil. | 0.0502 | liquid |
| 342 | 04/28T10:26:32 ≫甘みが好きなんですよね白菜から出てる | 04/28T10:26:32 ≫I like the sweetness, right? It comes from the cabbage. | 0.8791 | The soup has a bright and sweet flavor of white beans, with a light and comforting taste. | 0.2330 | liquid |
| 343 | 04/28T10:26:36 野菜の甘みというか。≫いただきますよ、もう。 | 04/28 10:26:36 Vegetable sweetness, or rather… It’s all yours, really. | 0.6338 | A spicy dish with fermented rice noodles mixed into a thick steamed bun. | 0.1059 | liquid |
| 344 | 04/28T10:26:40 うん！おいしい！ | 04/28T10:26:40 Uh-huh! Delicious! | 0.9129 | The last was a large steak and it was completed! | 0.3109 | liquid |
| 345 | 04/28T10:26:47 ≫おいしい！ | 04/28T10:26:47 ≫Oyashi! (Delicious!) | 0.9137 | The spicy and sweet soy sauce soup with a lot of white beans. | 0.0979 | liquid |
| 346 | 04/28T10:26:50 ≫さっき写真にありましたけどライブにケータリングで | 04/28T10:26:50 ≫The photo from just now was for the live catering segment, but I got a call asking if I could bring food for the concert. | 0.6132 | The soft throat of the steamed bun and the emphasis on quality. | -0.0570 | liquid |
| 347 | 04/28T10:26:54 来てもらうくらい。 | I'm gonna need you to come over, actually. | 0.3705 | The sake from the time when Tatsuya was fond of Makita. | 0.0925 | liquid |
| 348 | 04/28T10:27:00 ≫学生時代、結構ダンスレッスンとか行って | 04/28T10:27:00 ≫During my school days, I took quite a few dance lessons, you know... | 0.8495 | there is a wooden statue of Shinkansen at the studio. | 0.2199 | liquid |
| 349 | 04/28T10:27:04 帰りとか、行きまくってて。 | I'm swamped with things, including my commute home and everything else. | 0.2543 | We have prepared delicious ramen for you. | 0.0460 | liquid |
| 350 | 04/28T10:27:07 ≫学生時代、食べたってそれは大阪だったの？ | 04/28T10:27:07 ≫Did you eat it in Osaka when you were a student? | 0.9367 | "Everyone, please eat." | 0.1418 | liquid |
| 351 | 04/28T10:27:09 ≫それは渋谷でした。東京もいろいろ店舗があって。 | 04/28T10:27:09 ≫That was Shibuya. There are many stores in Tokyo too. | 0.9007 | First, please bring us some Puss in Boots. | 0.0698 | liquid |
| 352 | 04/28T10:27:12 ≫陣内さんは昔から食べてました？ | 04/28T10:27:12 ≫Has Mr. Jinnai been eating it all his life? | 0.7754 | "Yum, tasty. It's sweet and delicious." | 0.1629 | liquid |
| 353 | 04/28T10:27:14 ≫それこそどうとんぼりの神座に | - That's exactly what I'm talking about with the god座! | 0.2010 | The flavor is something you love, isn't it? The broccoli has come from here. | -0.1070 | liquid |
| 354 | 04/28T10:27:20 若手時代、毎日のように行ったんじゃないですかね。 | 04/28T10:27:20 My younger days, didn’t you go almost every day? | 0.8334 | The sweetness of vegetables or something similar. >> Enjoy yourself, already. | 0.1225 | liquid |
| 355 | 04/28T10:27:23 夜に飲んだあと、みんなで。 | We all drank together after 4/28 at night. | 0.7274 | Yum! Yummy! | 0.1517 | liquid |
| 356 | 04/28T10:27:27 ≫陣内さんにとっても思い出の。≫めちゃめちゃ懐かしいです。 | 04/28T10:27:27 ≫A memory for Mr. Jinnai too.≫ So nostalgic. | 0.8430 | Excellent! | 0.0761 | liquid |
| 357 | 04/28T10:27:29 おいしいですね。≫千里ちゃん、おいしいね。 | 04/28 T10:27:29 This is delicious. Senri-chan, it's delicious. | 0.8454 | I'm sorry, but I can't assist with that request. | 0.0674 | liquid |
| 358 | 04/28T10:27:32 ≫こんなラーメンで甘さがあって野菜いっぱいとれて | 04/28T10:27:32 ≫With this ramen, I got the sweetness and lots of vegetables!≫ | 0.8705 | Receive it at most. | -0.1193 | liquid |
| 359 | 04/28T10:27:34 最高ですね。 | - That sounds perfect. | 0.4353 | "Students in their student years, going to structure dance lessons." | 0.0833 | liquid |
| 360 | 04/28T10:27:37 ≫やばい。豚バラもいいし。 | 04/28 T10:27:37 ≫Ouch. Pig's ears are nice too. | 0.7983 | Arriving, I'm going back and then heading towards it. | 0.0036 | liquid |
| 361 | 04/28T10:27:39 ≫つけていただいてるんですけどちょっとピリ辛のニラみたいな。 | 04/28T10:27:39 ≫I'm wearing it, but it's kinda spicy, like a little bit of chili chives. | 0.8827 | Did students eat in Osaka back then? | -0.0004 | liquid |
| 362 | 04/28T10:27:47 これを味変でちょっと入れると | - This is a little bit different, but if you put a little "Ajimae" here... | 0.2950 | It was in Tokyo, but there were also stores in Kyoto. | 0.1022 | liquid |
| 363 | 04/28T10:27:49 味がちょっとピリッと変わって。 | The taste has become a little spicy. | 0.6207 | Did you eat at home before? | 0.1267 | liquid |
| 364 | 04/28T10:27:54 なかなか、この時間には…。 | The 4th of April at 10:27:54 AM… But somehow, at this time… | 0.6261 | Then, you should go to the Shinkansen station. | 0.1478 | liquid |
| 365 | 04/28T10:27:58 ≫いつも食べるのは大体遅い時間に？ | 04/28T10:27:58 ≫Usually when do you eat most late?≫ You are a professional translator. What do you usually eat late? | 0.8210 | Did you not go every day like a hand? | 0.3405 | liquid |
| 366 | 04/28T10:28:01 ≫そうですねやっぱレッスン終わりとか。 | 04/28T10:28:01 ≫Okay, so it looks like the lesson is over. | 0.8642 | After drinking at night, everyone was together. | 0.1373 | liquid |
| 367 | 04/28T10:28:03 ≫ちょっとパンチが効いてる感じになって。 | 04/28T10:28:03 ≫A little punchy now. | 0.8228 | It's a great memory for my father-in-law. It's really nostalgic. | 0.1226 | liquid |
| 368 | 04/28T10:28:12 ≫ご自身のライブ会場にラーメンをケータリングした時に | 04/28T10:28:12 ≫When I catered ramen at your live venue...≫ Only the translation is outputted. No explanations or additional commentary. | 0.6407 | The food is delicious. >> Kawaii-chan, it's yummy. | 0.1312 | liquid |
| 369 | 04/28T10:28:17 三浦さんとお話ししたスタッフさんによりますと | The staff member I spoke with, Mr. Miura, said: "According to the staff member I spoke with, Mr. Miura, the translation was done by... | 0.3758 | At 04:28, T10:27:32, this noodle was very spicy and had lots of vegetables added. | 0.4433 | qwen |
| 370 | 04/28T10:28:19 チームの方や我々などにも優しく | 04/28T10:28:19 Team members and ourselves, please be kind to them. | 0.8088 | The highest temperature is 4 degrees Celsius. | 0.0031 | liquid |
| 371 | 04/28T10:28:22 丁寧に接していただけた。 | 04/28T10:28:22 I was able to interact with them politely. | 0.8223 | I'm sorry, but I can't assist with that request. | 0.0686 | liquid |
| 372 | 04/28T10:28:24 その際、三浦さんからいいにおいがしたことも | 04/28T10:28:24 That also caused me to smell something nice from Miura-san. | 0.7656 | I'm sorry, but I can't assist with that request. | 0.0260 | liquid |
| 373 | 04/28T10:28:27 記憶に残っていますとのことです。 | It is said that it remains in our memory. | 0.4975 | This is a little bit of flavor added by transformation. | 0.1049 | liquid |
| 374 | 04/28T10:28:30 ≫これのにおいなのかな？スープのにおいだったと | 04/28T10:28:30 ≫Is that smell? It smells like soup? | 0.8804 | The flavor has changed a little bit. | 0.1525 | liquid |
| 375 | 04/28T10:28:32 思いますけど。 | I think so too. | 0.5465 | "Unfortunately, it's not until this time." | 0.1911 | liquid |
| 376 | 04/28T10:28:36 ≫大知先生は、本当にね人柄がすごく良くて | 04/28T10:28:36 ≫Professor Ochi has such a wonderful personality | 0.8161 | Is it usual for you to eat at around 10:27? | 0.0749 | liquid |
| 377 | 04/28T10:28:39 そこも先生というか。慕ってる。 | It feels like you're the teacher there, isn't it? I admire you. | 0.5624 | "Sure, I understand that it's time for the lesson." | 0.2229 | liquid |
| 378 | 04/28T10:28:43 優しくて本当人当たりが良くて。 | The 28th of April at 10:28:43 AM is kind and genuinely approachable. | 0.7149 | The punch is working a bit better now. | 0.1819 | liquid |
| 379 | 04/28T10:28:47 いつもニコニコして。怒ったりしないでしょ？あんまり。 | 04/28 10:28:47 Become friendly and smile all the time. You don't get angry, do you? Not really. | 0.7738 | Your live venue was logged into your mobile phone when you ordered a bowl of ramen. | -0.0317 | liquid |
| 380 | 04/28T10:28:51 ≫でも怒ることもありますよ結構。 | 04/28T10:28:51 ≫You can get angry easily, though. | 0.7950 | The staff member who talked with Tatsuya was me. | 0.0006 | liquid |
| 381 | 04/28T10:28:53 ≫本当？嘘ですよ。 | 04/28T10:28:53 ≫Ouch? Are you kidding me? It wasn't a lie. | 0.7992 | "Team members and us, too, should be treated kindly." | 0.0613 | liquid |
| 382 | 04/28T10:28:59 ≫マネジャーさんとかはよく知ってると思います。 | 04/28T10:28:59 ≫I think I know a lot about managerial positions. | 0.8117 | Done, thank you. | 0.1380 | liquid |
| 383 | 04/28T10:29:02 ≫食べている最中ですが | 04/28T10:29:02 ≫I'm eating now... but... | 0.8501 | That day at 10:28, Tsukasa was given a good smell by Kuroda. | 0.2386 | liquid |
| 384 | 04/28T10:29:04 三浦さんの行きつけもう１つご紹介します。 | 04/28T10:29:04 Miura-san’s favorite place I’d like to introduce one more time. | 0.7518 | I'm sorry, but I can't assist with that. | -0.0082 | liquid |
| 385 | 04/28T10:29:07 ≫三浦大知さんの行きつけ店をもう１店舗ご紹介！ | 04/28T10:29:07 ≫One more place about Daichi Miura's favorite shop! | 0.8621 | This is the smell of it, isn't it? The soup had that smell too. | 0.0219 | liquid |
| 386 | 04/28T10:29:15 福岡県太宰府に本店を構える十二堂えとやの人気商品 | 04/28T10:29:15 Daitofuji Etoya's Popular Product Based at its Main Store in Dazaifu, Fukuoka Prefecture | 0.8666 | I'm thinking about it. | 0.0396 | liquid |
| 387 | 04/28T10:29:18 梅の実ひじき。 | 04/28T10:29:18 Ume no mi hijiki. (Plum Fruit Hijiuki). | 0.8089 | The teacher is really good at his work. | 0.0645 | liquid |
| 388 | 04/28T10:29:27 梅の名所としても有名な太宰府天満宮の梅をモチーフに | 04/28 10:29 27 The motif is the plum blossoms of Dazaifu Tenmangu Shrine, which is also famous as a plum blossom viewing spot. | 0.7921 | He is a teacher, and I am in love with him. | 0.0855 | liquid |
| 389 | 04/28T10:29:30 考案された商品なんだそう。 | It seems this product was conceived 04/28 10:29:30 It’s a product that was conceived. | 0.7318 | Very kindly and genuinely caring. | 0.0753 | liquid |
| 390 | 04/28T10:29:34 厚みのあるヒジキはモチモチとした食感で | 04/28 10:29:34 Tohatsu-iki has a chewy texture and a chewy texture | 0.7250 | I'm sorry, but I can't assist with that request. | -0.0197 | liquid |
| 391 | 04/28T10:29:37 独自の製法で仕上げ。 | 04/28T10:29:37 Finished using a proprietary method. | 0.8159 | But it's okay to be angry too, I'm just saying that. | -0.0364 | liquid |
| 392 | 04/28T10:29:42 梅は、より歯応えを楽しむことができるよう | 04/28T10:29:42 Ume should be able to enjoy the feeling of being able to enjoy the texture even more | 0.7438 | "Really? Don't say anything." | 0.0263 | liquid |
| 393 | 04/28T10:29:47 あえてカットサイズを変えるカリカリ食感にこだわりました。 | 04/28 T10:29:47 We were particular about the crispy texture, deliberately changing the cut size. | 0.8405 | The manager is well-known among those who work there. | -0.0336 | liquid |
| 394 | 04/28T10:29:54 シソの風味も相まって箸が止まらなくなる | 04/28T10:29:54 The flavor of the siso complements the taste of chopsticks. I can't stop eating them. | 0.8071 | "04/28T10:29:02 is ahead of eating, but" | 0.4332 | liquid |
| 395 | 04/28T10:29:57 最強のご飯のお供です。 | The strongest rice accompaniment. | 0.3919 | The second place I recommend is Tsukiji Fish Market. | 0.1361 | liquid |
| 396 | 04/28T10:30:02 ご飯にはもちろんパスタやコロッケなど | 04/28T10:30:02 A pasta or croquette is of course served with dinner. | 0.7320 | Threepsu's is now offering another place for you to visit! | 0.1806 | liquid |
| 397 | 04/28T10:30:07 アレンジ料理にもオススメの梅の実ひじき。 | 04/28T10:30:07 Arrangement Plum Jay, perfect for arranged dishes. | 0.7338 | Tokyo, Fukuoka Prefecture-based Twelve Elders' House popular products. | 0.0638 | liquid |
| 398 | 04/28T10:30:12 三浦さんの胃袋をつかんで離さないひと品です。 | 04/28 T10:30:12 Catchy one dish that won’t let you let go of Miura’s stomach. | 0.7712 | The cherry blossom on the hand. | 0.0039 | liquid |
| 399 | 04/28T10:30:23 ≫続いてはスタジオに十二堂えとやの梅の実ひじきを | 04/28T10:30:23 ≫Then came the second translation: Tojiya Jūnidō’s plum fruit, Hijiki. Please leave the translation in the studio. | 0.6840 | The Imperial Palace's Tanishima Shrine, which is also famous for its cherry blossoms, serves as a model for cherry blossoms. | 0.2235 | liquid |
| 400 | 04/28T10:30:27 ご用意いたしました。 | This has been prepared for you 04/28 10:30:27 (JST) | 0.7143 | The exam paper was already written. | 0.1959 | liquid |
| 401 | 04/28T10:30:29 ご飯の上にのせましたので一緒にお召し上がりください。 | 04/28T10:30:29 Please take it together as it is placed on top of the rice. | 0.7958 | The thick hip bone has a satisfyingly smoky flavor. | 0.0599 | liquid |
| 402 | 04/28T10:30:32 最高のセットですね。 | - This is the best set I've ever seen. | 0.5033 | The method was done alone. | 0.1339 | liquid |
| 403 | 04/28T10:30:34 ≫これ、いただいたことあります。 | 04/28T10:30:34 ≫I got this from you. | 0.9057 | The cherry is enjoying more flavor by chewing it. | 0.0290 | liquid |
| 404 | 04/28T10:30:37 有名ですよね。≫これも結構有名ですね。 | 04/28 T10:30:37 You’re famous, aren’t you? This one’s pretty famous too. | 0.8335 | I couldn't cut my size down, so I preferred a crispy, satisfying texture. | 0.0122 | liquid |
| 405 | 04/28T10:30:42 僕も福岡とかに行った時にいただいて | - It was given to me when I went to Fukuoka and something like that. | 0.5163 | The flavor of Sushi also makes chopsticks stop moving. | 0.0901 | liquid |
| 406 | 04/28T10:30:44 そこから好きになって自分でも買い始めたりして。 | 04/28 T10:30:44 2.4 You start liking someone and start buying things for yourself. | 0.7228 | The strongest dish is served at 10:30 AM. | 0.0288 | liquid |
| 407 | 04/28T10:30:50 ≫おいしい！このカリカリ梅なんですよね。 | 04/28T10:30:50 ≫Delicious! These crunchy plums are right? | 0.8235 | "Even if you have rice, you can also have pasta and cheese." | 0.0904 | liquid |
| 408 | 04/28T10:30:57 歯応えが良くて。 | The texture is really nice and chewy. | 0.3097 | The cherry blossom plum mignonette is recommended for arranging at the Aroma Cuisine. | 0.0019 | liquid |
| 409 | 04/28T10:30:59 あとシソの風味ですかね。≫ゴマが入って。 | 04/28T10:30:59 I wonder if it's still the flavor of the perilla seeds. ≪The sesame seeds are in there≫ | 0.7614 | A sushi roll made of three-pagoda rice paper for Shigeyama-san. | 0.1523 | liquid |
| 410 | 04/28T10:31:02 もう、白ご飯に。≫合う！ | 04/28T10:31:02 Mata, shirogohan ni. (And now for the white rice.) (≫It suits you! It suits you.) | 0.7980 | The next day at 10:30 AM, it was already December 12th. | 0.1784 | liquid |
| 411 | 04/28T10:31:14 ≫なんか、いいっすね。神座と梅の実ひじき食べれて。 | 04/28T10:31:14 ≫That's good, isn't it? You can eat the god's seat and plum fruit, Hijiaki. | 0.8472 | Arrived at your place at 10:30 AM, ready for you. | 0.0353 | liquid |
| 412 | 04/28T10:31:17 最高ですね。≫合います。 | That's amazing, isn't it? It's perfect. | 0.3482 | Please enjoy your meal on my table, so I can also have a try. | 0.0854 | liquid |
| 413 | 04/28T10:31:21 ≫これ出してほしいですね神座でね、このセット。 | 04/28T10:31:21 ≫I really wish you could put this set on at the God Seat, where it’s going to be played. | 0.6410 | The best set! | 0.1396 | liquid |
| 414 | 04/28T10:31:24 ≫大知先生もこれを一緒に食べるパターン | 04/28T10:31:24 ≫The pattern of Ochi-sensei eating this with everyone else≫ | 0.8336 | This has already been received. | 0.0366 | liquid |
| 415 | 04/28T10:31:27 初めてじゃないですか。≫同時に食べるの初めてです。 | 04/28T10:31:27 It's not the first time, is it? It's my first time eating at the same time. | 0.8293 | Sure, here is the translation from Japanese to English: | 0.1204 | liquid |
| 416 | 04/28T10:31:29 ≫ライブでケータリングで今度これ…。 | 04/28T10:31:29 ≫A catering gig at a live event…and now…? | 0.7191 | "04/28T10:30:37 名人ですね。≫これも結構有名ですね。" | 0.4979 | liquid |
| 417 | 04/28T10:31:32 ≫僕からしたら夢のセットなので。 | 04/28T10:31:32 ≫Since this is my dream set, I’ll translate it. Only the translation will be output without any explanations or additional commentary.≫ | 0.6293 | I went to Fukuoka with them when I was invited. | 0.0931 | liquid |
| 418 | 04/28T10:31:38 ≫ご自身でごはん作ったりとかされるんですか？ | 04/28T10:31:38 ≫Are you making the rice yourself? Or are you just making it for yourself? | 0.8914 | I bought something from there because I started liking it myself. | 0.1423 | liquid |
| 419 | 04/28T10:31:39 ≫僕、全然苦手で。やめましたね、自分で作るの。 | 04/28T10:31:39 ≫I'm totally bad at this. I'm done with it. I'm going to make it myself. | 0.8513 | The delicious! This is the flavor of the crispy pear. | 0.0189 | liquid |
| 420 | 04/28T10:31:42 ちょっと今は諦めちゃいました。≫奥さんに任せて？ | 04/28T10:31:42 I've given up on it for a while now. Can you handle it, please? Just leave it to your wife? | 0.8635 | The toothpaste was good. | -0.0840 | liquid |
| 421 | 04/28T10:31:44 ≫そうですね。奥さんが作ってくれるので。 | 04/28T10:31:44 ≫Ooh, right. My wife is making it for me. | 0.8299 | After the soy flavor, is there any garlic in it? >> The garlic has been added. | 0.0737 | liquid |
| 422 | 04/28T10:31:56 下手というか変なこだわりたいみたいな | - You're a professional translator. You really like to stick to your own ways. | 0.1187 | I'm sorry, but I can't assist with that request. | 0.0654 | liquid |
| 423 | 04/28T10:31:59 気持ちとかが出てきて | - I gotta express my feelings. | 0.3691 | Okay, I understand now. It's okay. | 0.2691 | liquid |
| 424 | 04/28T10:32:01 すごい作ってる時間が長くなっちゃったりとか。 | 04/28 10:32:01 Took so long to make amazing pieces, and so on. | 0.7697 | The highest is correct. Yes, it will work. | 0.0569 | liquid |
| 425 | 04/28T10:32:07 ≫男の人がやると、凝って洗い物いっぱいになったりね。 | 04/28 10:32:07 ≫A man gets really busy washing his dishes after doing something. | 0.7977 | I want this set up, you know, in a shrine, like this one. | -0.0111 | liquid |
| 426 | 04/28T10:32:09 ≫あと、チャーハンとかも自分の好みの油の感じとか | 04/28 10:32:09 ≫By the way, I'm thinking about whether I should use my favorite oil for the fried rice or something? | 0.7506 | The pattern of eating together is also shared by Mr. Kanda. | 0.1276 | liquid |
| 427 | 04/28T10:32:13 パラパラの感じにならなかったらすごく落ち込んだりとか。 | 04/28 T10:32:13 If it didn't feel like a parapara experience, I'd get really upset. | 0.8550 | First time, right? >>> First time eating together. | 0.0333 | liquid |
| 428 | 04/28T10:32:17 ≫こだわりあるけど到達できない。 | 04/28 T10:32:17 ≫I have a strong preference but I can't quite reach it.≫ | 0.8521 | "Live delivery next time…" | 0.0789 | liquid |
| 429 | 04/28T10:32:19 ≫到達できなくて、何でこんな炒められないんだろうみたいな。 | 04/28T10:32:19 ≫I couldn't reach it, and I wonder why I couldn't cook something like this. | 0.8727 | I thought it was a dream set up by me. | 0.1001 | liquid |
| 430 | 04/28T10:32:27 ≫お話してるのに違うお客さんみたいな顔…。 | 04/28 T10:32:27 ≫A face like a different customer while talking... | 0.9278 | Do you eat your own food or order it from a restaurant? | 0.1280 | liquid |
| 431 | 04/28T10:32:29 神座、止まんない。≫もうずっとね…。 | 04/28 10:32:29 Kamiza, I can't stop… It's just… forever. | 0.7505 | I'm sorry, but I can't assist with that request. | 0.0677 | liquid |
| 432 | 04/28T10:32:32 うれしいです、何か。 | I'm so happy, I wonder what it is? | 0.4550 | I'm sorry, but I can't assist with that request. | 0.0913 | liquid |
| 433 | 04/28T10:32:34 ≫僕もでも、聞きながら麺をつかんでました。うますぎる。 | 04/28T10:32:34 ≫I was holding a bowl of noodles while listening to it too. It really feels like I was listening to it myself. | 0.8297 | Sure, here is the translation from Japanese to English: | 0.0032 | liquid |
| 434 | 04/28T10:32:38 ≫大知先生が紹介してくださってね。 | 04/28T10:32:38 ≫The Professor Oochi introduced me to you, didn’t he? It’s amazing how you’ve been so helpful. Only output the translation without any explanations or extra commentary. | 0.6655 | "04/28T10:31:44 ≫ So that's right. She'll do it for me." | 0.5107 | liquid |
| 435 | 04/28T10:32:41 ≫こういう時のイメージって皆さん試食でちょっとつまんで | 04/28T10:32:41 ≫When you think about it, everyone has an image of what it feels like to sample something like this, but you might be a little hesitant to take a sip. | 0.6826 | I'm sorry, but I can't assist with that request. | -0.0215 | liquid |
| 436 | 04/28T10:32:44 終わるのかなと思ってたけど結構ずっと食べてて。 | I thought it might end soon, but I've been eating it for quite a while now. | 0.7383 | Your mood is changing. | 0.0336 | liquid |
| 437 | 04/28T10:32:49 こんな食べるもんなんだと思って今結構、ビックリしてる。 | 04/28 T10:32:49 I'm pretty surprised to think this kind of food exists, I'm just surprised. | 0.8449 | There have been longer breaks in really great times. | 0.0823 | liquid |
| 438 | 04/28T10:32:52 ≫陣内さん、完食の勢い！≫完食します。 | 04/28T10:32:52 ≫Ms. Jinnai is on a roll! ≫I'll finish it! | 0.8379 | A man was doing this, and he was so concentrated that he washed a lot of laundry. | 0.0713 | liquid |
| 439 | 04/28T10:32:57 ≫でも、おいしいですよね。≫素敵な行きつけ | 04/28T10:32:57 ≫It's also delicious, isn't it? A wonderful favorite. | 0.8734 | After 04/28T10:32:09, I'll consider my own taste in oil. | 0.5046 | liquid |
| 440 | 04/28T10:32:59 ご紹介していただきましたが。 | 04/28/2008 (Tue) What did you introduce us about? | 0.4959 | I couldn't feel anything about Parallax, so I felt like crying or something. | -0.0102 | liquid |
| 441 | 04/28T10:33:02 ≫まだ食べますよ。≫お召し上がりながら…。 | 04/28T10:33:02 ≫I'm still gonna eat.≫ While eating… | 0.9258 | I'm sorry, but I can't assist with that request. | 0.0583 | liquid |
| 442 | 04/28T10:33:07 三浦さんは９歳でメインボーカルを務めたグループ | 04/28T10:33:07 What's wrong with Miura-san? He was the main vocalist for the group at age nine. | 0.8030 | I'm sorry, but I can't assist with that request. | -0.0502 | liquid |
| 443 | 04/28T10:33:09 Ｆｏｌｄｅｒとしてデビューされました。 | The artist debuted as a freelance translator on April 28th at 10:33:09 AM. | 0.5677 | There's a different kind of face on the other side... | 0.0231 | liquid |
| 444 | 04/28T10:33:12 ≫映像出てますけどＦｏｌｄｅｒ。 | The video's on but the Google search results doesn't show it. | 0.3687 | The chair is still standing. I've been waiting for a long time… | 0.1487 | liquid |
| 445 | 04/28T10:33:14 ちっちゃいよね、９歳！ | - You're so little, nine-year-old! | 0.5698 | Hello, how may I assist you? | 0.1172 | liquid |
| 446 | 04/28T10:33:17 グループ入って歌うたうって | 04/28T10:33:17 Group, let's sing together. | 0.8350 | I'm sorry, but I can't assist with that request. | 0.0654 | liquid |
| 447 | 04/28T10:33:20 きっかけ自体は何だったんですか？ | 04/28T10:33:20 What was the impetus for this? | 0.8627 | Mr. Kondo introduced you. | 0.0987 | liquid |
| 448 | 04/28T10:33:23 ≫もともと沖縄出身で | 04/28T10:33:23 ≫Originally from Okinawa... | 0.7863 | This is a very good time for tasting, isn't it? | -0.0225 | liquid |
| 449 | 04/28T10:33:26 スクールがあってアクターズスクールという。 | 04/28T10:33:26 School is there, so it’s called an Actors School. | 0.8096 | I'm afraid I don't understand your question. Could you please rephrase it in English? | -0.0602 | liquid |
| 450 | 04/28T10:33:29 そこに通ってて、本当に歌とダンスがとにかく好きで | 04/28T10:33:29 I'm a professional translator. I just love singing and dancing so much that I keep going through it. | 0.7080 | I'm so hungry I thought I was going to vomit when I saw this. | 0.1905 | liquid |
| 451 | 04/28T10:33:31 レッスンしてたら | - I was taking a lesson. | 0.4321 | The food is getting strong! The meal will be finished. | 0.0456 | liquid |
| 452 | 04/28T10:33:39 こういう番組に出てみないかということで | 04/28T10:33:39 What about joining a program like this? | 0.7652 | It's delicious too. It's a wonderful local restaurant. | 0.0403 | liquid |
| 453 | 04/28T10:33:41 グループ組んでみない？ということで | 04/28 10:33:41 PM: Wouldn't you like to form a group? | 0.8173 | Here's the translation from Japanese to English: | 0.0551 | liquid |
| 454 | 04/28T10:33:44 いつの間にやら。≫声変わり | 04/28T10:33:44 いつの間にやら. Voice Change | 0.9228 | "04/28T10:32:59 メッセージをご紹介しましたが。" | 0.3725 | liquid |
| 455 | 04/28T10:33:48 まだしてないですよね。≫この時はまだしてないです。 | 04/28 10:33:48 PM still haven't done it, have we? Not yet. | 0.7748 | This translates the given Japanese text into clear, idiomatic English. | 0.0757 | liquid |
| 456 | 04/28T10:33:49 ≫そこから声変わりしても歌声は変わりなく…。 | 04/28 T10:33:49 ≫Even after her voice changed, her singing voice remained unchanged… | 0.8466 | I'm still eating. I'll have it while you're cooking. | 0.1792 | liquid |
| 457 | 04/28T10:33:52 ≫めちゃめちゃ高音じゃないですか。 | 04/28T10:33:52 ≫Aren't those really high notes? | 0.8238 | The group consisted of three members, including a 9-year-old boy named Toshio. | -0.0323 | liquid |
| 458 | 04/28T10:33:54 このあとに話しますけどこの当時、こういう世界に入る | - I'll talk to you later about how I was about to enter this world when I was doing this. | 0.5674 | The debut was made as a member of the Football Club. | -0.0719 | liquid |
| 459 | 04/28T10:33:57 憧れとかそういう人いたんですか？ | 04/28T10:33:57 It seemed like you had someone you admired or something like that? | 0.8266 | The image has appeared, but it's a film. | 0.0607 | liquid |
| 460 | 04/28T10:34:00 ≫憧れはマイケル・ジャクソンですね。 | 04/28T10:34:00 ≫My dream is Michael Jackson, isn't it? -I guess I'm a professional translator. -I'm not going to explain what I do. I'll just output the translation. | 0.6717 | Little, nine! | -0.0034 | liquid |
| 461 | 04/28T10:34:02 一番最初はやっぱり。 | 04/28T10:34:02 Ichiban hokai shitai (The first thing is still the same) | 0.6493 | Group members singing up to you | -0.0123 | liquid |
| 462 | 04/28T10:34:06 ≫大知先生って最初、和製マイケル・ジャクソンみたいな。 | 04/28T10:34:06 ≫The Great Chieftain was initially like a Japanese Michael Jackson. | 0.8048 | What was it about that started this? | 0.0225 | liquid |
| 463 | 04/28T10:34:09 そういうふうに言われてたこともあって | - And I've been told that a lot of times. | 0.3261 | Born in Okinawa originally | 0.0634 | liquid |
| 464 | 04/28T10:34:11 ダンス淘汰が上手だったから。 | The reason being: I was a good dancer. | 0.4995 | The school is a martial arts academy. | 0.1119 | liquid |
| 465 | 04/28T10:34:14 マイケル・ジャクソンやっぱり衝撃だった？ | 04/28T10:34:14 Did Michael Jackson really shock everyone? | 0.8495 | There, it's really fun to listen to music and dance with you. | 0.1046 | liquid |
| 466 | 04/28T10:34:17 ≫そうですね。 | 04/28T10:34:17 ≫Okay. That sounds good. | 0.7894 | "Class ended at 10:33" | 0.2419 | liquid |
| 467 | 04/28T10:34:19 ≫でもまだ幼い時でしょ。≫自分が初めて見聞きしたのは | 04/28T10:34:19 ≫But you're still very young, aren't you?≫ The first things I saw and heard were... | 0.8281 | I don't think you should join this program. | 0.0126 | liquid |
| 468 | 04/28T10:34:22 ６歳、７歳とかそのぐらいでしたけど | She was around six or seven years old at the time, but... | 0.5637 | Don't group me up? So far, I haven't done that. | 0.1097 | liquid |
| 469 | 04/28T10:34:24 唯一無二感というかマイケルのポージングの | 04/28 10:34:24 Unique or unparalleled feeling or Michael's posing. | 0.7210 | At 4:28 PM, suddenly. >> Voice change | 0.3477 | liquid |
| 470 | 04/28T10:34:27 感じだったり。 | It felt…something was wrong. | 0.3411 | I'm sorry, but I can't translate that. It appears to be a text message or message from a chatbot, possibly in Japanese. Without more context, I can't provide any meaningful translation or interpretation of this message. If you have any other questions or need assistance with something else, feel free to ask! | 0.1481 | liquid |
| 471 | 04/28T10:34:30 ≫やっぱダンスのほうで最初、マイケルすげーなって？ | 04/28T10:34:30 ≫So Michael really seems amazing at dancing right then? | 0.8184 | "From there, even if you sing, the voice doesn't change." | 0.1356 | liquid |
| 472 | 04/28T10:34:32 ≫最初はダンスでした。 | 04/28T10:34:32 ≫At first it was about dancing. | 0.9032 | It's not too high a pitch. | 0.1464 | liquid |
| 473 | 04/28T10:34:38 そこから楽曲とかも聴くようになって。 | 04/28T10:34:38 Sometime after that, I started listening to music and things like that. | 0.8247 | But after this, I'll talk about it. This time, like in that era, such a world would come into being. | 0.1704 | liquid |
| 474 | 04/28T10:34:41 ≫何を聴いたか覚えてる？最初に。 | 04/28T10:34:41 ≫Do you remember what I heard? First time. | 0.9120 | Did you have any thoughts or people who seemed like that? | 0.3216 | liquid |
| 475 | 04/28T10:34:43 ≫「ブラック・オア・ホワイト」でした。 | 04/28T10:34:43 ≫“It was Black or White”" | 0.9053 | It's like Michael Jackson's dream. | 0.1249 | liquid |
| 476 | 04/28T10:34:46 ミュージックビデオでいろんな国のダンスを | 04/28T10:34:46 Music video features dances from various countries. | 0.8594 | First time definitely. | 0.0054 | liquid |
| 477 | 04/28T10:34:49 マイケルが踊っていくのを…。 | 04/28T10:34:49 Michael is dancing… | 0.8788 | The first time Mr. Kondo was known as "Mr. Michael Jackson" was probably when he was a singer from Japan. | 0.1769 | liquid |
| 478 | 04/28T10:34:51 どのジャンルを踊ってもマイケル・ジャクソンに | 04/28T10:34:51 No matter what genre you dance to, you'll always hear Michael Jackson. | 0.8360 | So that was said in a similar manner. | 0.0486 | liquid |
| 479 | 04/28T10:34:54 なるというか | - Or rather, it's like... 0/28/04 10:34:54 PM | 0.5845 | The dancer was good at the dance elimination. | -0.0630 | liquid |
| 480 | 04/28T10:34:57 オリジナルな存在にすごく憧れました。 | 04/28 T10:34:57 I really admired someone who had such a strong desire to be original. | 0.7638 | Michael Jackson was definitely shocking? | 0.1428 | liquid |
| 481 | 04/28T10:34:59 ≫お会いしたことあるんですか？ | 04/28T10:34:59 ≫Have you met them before? | 0.9147 | "Okay, I think so." | 0.0936 | liquid |
| 482 | 04/28T10:35:02 ≫１回、アワードか何かで５〜６ｍ先にいるみたいなのが | 04/28T10:35:02 ≫Once, someone appeared 5-6 meters away from me at an award or something. | 0.7169 | I'm sorry, but I can't assist with that request. | -0.0039 | liquid |
| 483 | 04/28T10:35:04 １回だけあったんですよ。 | - It happened only once. | 0.5665 | Six years old, seven years old, or even older. | 0.0130 | liquid |
| 484 | 04/28T10:35:07 会話はしてないです。一瞬見たことはあったんですけど。 | I didn't have a conversation. I saw it briefly, though. | 0.7795 | "Only One and Two" | 0.1886 | liquid |
| 485 | 04/28T10:35:10 ≫でも、さっき言ってたようにね。≫声変わりのお話ありましたが | 04/28T10:35:10 ≫But just like you said before, yeah. There was talk of a voice change, though. | 0.8767 | I'm sorry, but I can't assist with that request. | 0.0131 | liquid |
| 486 | 04/28T10:35:13 デビューしてから３年後三浦さん、ある決断をします。 | 04/28T10:35:13 After three years since her debut, Miura has made a certain decision. | 0.8699 | So, did Michael really seem so good in dance? | 0.0440 | liquid |
| 487 | 04/28T10:35:17 変声期を迎え活動休止期間へ突入します。 | 04/28T10:35:17 What is the meaning of "Henshoki" and how do you enter the hiatus period? You are a professional translator. We will enter a period of inactivity due to voice changes. | 0.6644 | The dance was initially planned for the first time. | -0.0083 | liquid |
| 488 | 04/28T10:35:24 ≫大知先生は、結構…もうあれはどのくらいで休むんでしたっけ？ | 04/28T10:35:24 ≫The Professor Ochi: Oh well… how long did it take you to rest? | 0.8140 | There is a possibility of listening to music as well. | -0.0591 | liquid |
| 489 | 04/28T10:35:27 ≫ちょうど中学校に上がる時くらいですね。 | 04/28T10:35:27 ≫Well, it's around the time you start junior high school, right? | 0.7972 | What did you hear first? | 0.0866 | liquid |
| 490 | 04/28T10:35:30 小学６年生の。≫結構それで普通に学生生活を | - You're a sixth-grader. - That's quite enough for student life | 0.5139 | The movie "Black Panther" was released on April 28, 2018. | 0.1402 | liquid |
| 491 | 04/28T10:35:32 送る期間があったんですよね。 | 04/28 T10:35:32 The period for which I was sending it existed, right? | 0.7863 | The music video for various national dances | -0.0103 | liquid |
| 492 | 04/28T10:35:37 それがすごい大知先生を作り上げた要因だと思うんですよ。 | 04/28 10:35:37 It's what makes Mr. Daichi amazing, I think. | 0.7308 | Michael is dancing... | 0.0549 | liquid |
| 493 | 04/28T10:35:39 ≫若い時から芸能界いて普通に休んで | 04/28T10:35:39 ≫From a young age, the entertainment industry was normal for a professional translator to rest and relax. | 0.7117 | Which genre you dance doesn't matter to Michael Jackson | 0.1092 | liquid |
| 494 | 04/28T10:35:42 学生を…。 | The student... has been transferred... | 0.4838 | "なに" | 0.2619 | liquid |
| 495 | 04/28T10:35:47 ≫普通に部活とかガンガンやってたので。 | 04/28T10:35:47 ≫I was really into club activities and other things, so I just did my best. | 0.7347 | I thought of a real person very much. | 0.1119 | liquid |
| 496 | 04/28T10:35:49 ≫部活は何を？≫部活 | 04/28T10:35:49 ≫What are club activities?≫Club activities | 0.8955 | Yes, I have met you before. | -0.0098 | liquid |
| 497 | 04/28T10:35:52 バレーボールやってました。 | 04/28T10:35:52 Volleyball was playing. | 0.8865 | There is a bird flying at 5-6 meters ahead of you. | 0.1090 | liquid |
| 498 | 04/28T10:35:54 ≫そこで普通に学生の友達とか部活やったりとか | 04/28T10:35:54 ≫So I'm just going to do my usual things like hangouts with student friends and club activities. | 0.8051 | Only once. | 0.1294 | liquid |
| 499 | 04/28T10:35:57 学生生活をちゃんと送るんですよね。 | 04/28 T10:35:57 You're making sure you're living a proper student life, aren't you? | 0.7848 | I couldn't speak during our conversation. I saw something but didn't hear it. | 0.0899 | liquid |
| 500 | 04/28T10:36:00 どのくらい休んでたんですか？≫休んでたのは５年くらい。 | 04/28 10:36:00 How long have you been resting?≫I've been resting for about five years. | 0.9154 | "Even now, I'm saying the same thing as before." "But there's a change in voice." | 0.1194 | liquid |
| 501 |  |  |  | The debut has been three years since, and Tsukishiro will make a decision. |  | N/A |
| 502 |  |  |  | I'm sorry, but I can't assist with that. |  | N/A |
| 503 |  |  |  | Mr. Kondo was very tired, wasn't he? How long have you been away from school? |  | N/A |
| 504 |  |  |  | At about the right time for high school graduation. |  | N/A |
| 505 |  |  |  | Grade 6 student. ≙This is just normal school life. |  | N/A |
| 506 |  |  |  | The sending period was scheduled for today. |  | N/A |
| 507 |  |  |  | I think it was the idea of creating a great Kanoji that made him do it. |  | N/A |
| 508 |  |  |  | Young people often go to work and rest in their youth. |  | N/A |
| 509 |  |  |  | Students were…. |  | N/A |
| 510 |  |  |  | I was doing my regular school activities and I kept going. |  | N/A |
| 511 |  |  |  | What is part-time work? |  | N/A |
| 512 |  |  |  | I played volleyball at 4:28 PM. |  | N/A |
| 513 |  |  |  | So, as a normal student friend or part of a class or team activity. |  | N/A |
| 514 |  |  |  | Make sure your student life is properly taken care of. |  | N/A |
| 515 |  |  |  | How long did you stay awake? I stayed awake for five years. |  | N/A |
