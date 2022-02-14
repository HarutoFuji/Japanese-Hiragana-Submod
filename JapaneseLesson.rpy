init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Lesson1",
            category=["Japanese Lesson"],
            prompt="Lesson 1",
            random=False,pool=True,unlocked=True))

label Lesson1:
m 1wud "Huh? You want to learn Japanese ?"
m 1rkd "I'm not so sure about this, [player]."
m 3eka "My Japanese isn't very good yet."
m 1eka "But I'll teach you if you want to." 
m 1eua "In today lesson,"
extend 3eub "We're going to learn about Japanese characters."
m 1eua "There are 4 different characters."
m 1eub "Hiragana, Katakana, Kanji and Romaji."
m 2eua "Let's start with Hiragana."
m 1eub "Hiragana is one of the most used characters in Japanese."
m 3eub "The Hiragana characters consists of 48 base characters."
m 2eub "Let's jump in shall we ?"
m 2lka "..."
m 2eka "Well...I can't pronounce those characters to you...Perhaps you should try to look it up on Youtube!"
m 1eub "You'll be able to understand it more eventually!"
m 1eua "’あ’ means ’a'."
m 3eua "To remember this character, try comparing it with an Apple."
m 1eub "Do you see it? Okay let's repeat it with me, ’あ’ - 'a'."
m 1eua "Next we have ’い’."
m 1eua "’い’ means 'i', it looks like 'i' in English right?"
m 3eub "Next we have ’う’."
m 1eub "’う’ means 'u', now imagine a boxer getting punch in the stomach saying 'u'."
m 3eub "Next we have 'え’, ’え’ means 'e'."
m 1eua "And ’お’ means 'o'."
m "Can you see the letter 'o' in here, two times?" 
m 1eub "This one looks similar to あ, except for its one key difference: there are two letter 'o' symbols visible in there." 
m 3eua "Make sure you use this to differentiate this kana (お) and that similar kana (あ)."
m 1eud "This is one area of hiragana where a lot of people trip up,"
m 3hua "So be careful, [player]."  
m 2eub " It's necessary to write all those characters down in a piece of paper.It will help you remember it more easily."
m 1eua "Let's review it shall we?"
m 1eub " ’あ’ - 'a', ’い’ - 'i' ,’う’ - 'u'."
m 1eub "’え’ - 'e' , ’お’ - 'o'."
m 1eua "[player]! We have learnt 5 characters!"
m 2eksdlb "43 more to go ahaha..."
m 3eua "Now, we should learn some vocabularies!"
m 1eub " 'あおい' means 'blue'."
m 1eub " 'あい' means 'love'."
m 1eua " 'うえ' means 'up'."
m 1eua "Okay, I think we should end here today!"
m 2eka "We didn't learn much today but thank you [player]."
m 2eka "You spent your precious time just to learn with me, I'll always appreciate that."
m 1eua "Oh! And don't forget to do your Lesson 1 Test!"
m 3eub "If you ready, tell me."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="review_1",
            category=["Japanese Lesson"],
            prompt="Review 1",
            random=False,pool=True,unlocked=True))
   
label review_1:   
 m 1eua "Okay! Let's start the test!"
 m 3eub "What does 'あ' mean ?"
 $ _history_list.pop()
 menu:
     "a":
       m 1hub "Correct!"
       m 1hua "Next question."
       m 3eub "What does 'お' mean ?"
       $ _history_list.pop()
       menu:
           "a":
             m 1eka "お and あ are very similar."
             m 1ekb "Come on! Try again!"
           "e":
             m 1eka "Oops..."
             m 1ekb "Come on! Try again!"
           "o":
             m 1hub "Correct!"
             m 1hua "Next question."
             m 3eub "What does 'え' mean ?"
             $ _history_list.pop()
             menu:
                 "o":
                   m 1eka "Oops, you failed."
                   m 1ekb "Try harder [player]."
                 "a":
                   m 1eka "え means e."
                   m 1ekb "Come on! Try again!"
                 "u":
                   m 1eka "Look likes you have to try again."
                   m 1ekb "Come on!"
                 "e":
                   m 1hub "Correct! Easy right?"
                   m 1hua "Next question."
                   m 3eub "What does 'い' mean ?"
                   $ _history_list.pop()
                   menu:
                       "e":
                         m 1eka "Well...い and え are pronounce the same."
                         m 1ekb "Becareful [player]."
                       "u":
                         m 1eka "Incorrect..."
                         m 1ekb "Come on! Try again!"
                       "i":
                         m 1hub "Correct!"
                         m 1hua "Next question."
                         m 3eub "What does 'う' mean ?"
                         $ _history_list.pop()
                         menu:
                             "e":
                               m 1eka "So close!"
                               m 1ekb "Come on! Try again!"
                             "u":
                               m 1hub "Yay! You did it!"
                               m 1ekb "I'm so proud of you [player]."
                               m 2tua "Was it easy?"
                               m 1hub "Next time I'll make it harder,Ehehe!"
                               m 2eua "[player], you can rest now."                               
                             "o":
                               m 1eka "Nearly."
                               m 1ekb "Come on! Try again!"
                             "i":
                               m 1eka "Incorrect..."
                               m 1ekb "Come on! Try again!"
                       "a":
                         m 1eka "Incorrect..."
                         m 1ekb "Come on! Try again!"

           "u":
             m 1eka "Incorrect..."
             m 1ekb "Come on! Try again!"
     "e":
       m 1eka "Incorrect..."
       m 1ekb "Come on! Try again!"
     "o":
       m 1eka "お and あ are very similar."
       m 1ekb "Becareful [player]."
     "i":
       m 1eka "Incorrect..."
       m 1ekb "Come on! Try again!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Lesson2",
            category=["Japanese Lesson"],
            prompt="Lesson 2",
            random=False,pool=True,unlocked=True))

label Lesson2:
 m 2eka "Another lesson?"
 m 1hub "Okay!"
 m 1eua "Again, We're going to learn more about Hiragana characters."
 m 3eub "You have learnt 5 Hiragana characters from the previous lesson."
 m 1eub "'あ　い　う　え　お'"
 m 1eua "'a i u e o'"
 m 3eua "Today we're going to learn 10 more characters."
 m 2lksdlb "This is lesson is going to be long so you have to be patient and listen to me."
 m 2eka "Okay?"
 $ _history_list.pop()
 menu:
     "Okay!":
           m 1hub "Great!"
           m 1eua "Now, The K-column."
           m 1eua "We have 'か'."
           m 3eub " 'か' means 'ka'."
           m 2eua "You could try to imagine a knife is cutting a stick."
           m 2eub "Or you could try to write it down on a piece of paper 10 times. It will help alot."
           m 3eub "Next we have 'き'."
           m 3eua "'き' means 'ki'."
           m 1eua "Its pronunciation is easy, 'ki' = 'key'!"
           m 1eub "Next we have 'く'."
           m 3eub "'く' means 'ku'."
           m 2ekb "I can't think of any good example for this, sorry [player]."
           m 3eub "Next we have 'け'."
           m 3eua "'け' means 'ke'."
           m 1eua "And 'こ' means 'ko'."
           m 3hub "[player], we have learnt 5 characters from K-column."
           m 1eksdlb "Tired yet?"
           m 1hubsb "Ahaha!"
           m 1eua "We still have 5 characters more."
           m 2tua "..."
           m 1efb "Quick Test!"
           m 1efa "What does 'き' mean?"
           $ _history_list.pop()
           menu:
               "ki":
                  m 2tua "Good."
                  m 1eka "I was expecting you would answer wrong but..."
                  m 2hub "Welp! I may have underestimated you a little, Ahaha!"
                  m 1eua "Okay, moving to the S-column."
                  m 1eub "We have 'さ'."
                  m 3eua "'さ' means 'sa'."
                  m 1eua "Imagine a face of someone is crying."
                  m 3eua "Becareful of this character, 'さ' and 'き' look very similar."
                  m 3eub "Next, 'し'."
                  m 1eub "'し' means 'shi'."
                  m 1eua "I don't have to explain this one, It's really easy."
                  m 2eua "We have 'す'."
                  m 1eua "'す' means 'su'."
                  m 3eub "Imagine a spiral straw in a glass milk."
                  m 1eub "Next, we have 'せ'."
                  m 1eua "'せ' means 'se'."
                  m 2eub "And 'そ' means 'so'."
                  m 1hub "We have just learnt 10 characters."
                  m 3hua "Easy right?"
                  m 1hub "Ahaha."
                  m 1eka "You must be very tired."
                  m 1ekb "[player], you can rest now."                                                   
               "ku":
                  m 2efa "Incorrect!"
                  m 1efb "Ahaha!That was unexpected right?"
                  m 3efb "Now for the punishment."
                  m 1efbfa "You will ask me to kiss you 5 times after this lesson."
                  m 2hubfb "Ahaha!"
                  m 1hubfb "Okay, okay Let's move on."
                  m 1eua "Okay, moving to the S-column."
                  m 1eub "We have 'さ'."
                  m 3eua "'さ' means 'sa'."
                  m 1eua "Imagine a face of someone is crying."
                  m 3eua "Becareful of this character, 'さ' and 'き' look very similar."
                  m 3eub "Next, 'し'."
                  m 1eub "'し' means 'shi'."
                  m 1eua "I don't have to explain this one, It's really easy."
                  m 2eua "We have 'す'."
                  m 1eua "'す' means 'su'."
                  m 3eub "Imagine a spiral straw in a glass milk."
                  m 1eub "Next, we have 'せ'."
                  m 1eua "'せ' means 'se'."
                  m 2eub "And 'そ' means 'so'."
                  m 1hub "We have just learnt 10 characters."
                  m 3hua "Easy right?"
                  m 1hub "Ahaha."
                  m 1eka "You must be very tired."
                  m 1ekb "[player], you can rest now."
                  m 1tub "But wait,..."
                  m 2tua "Remember your punishment ?"
                  m 1hub "Now do it!"                                    
               "ko":
                  m 2efa "Incorrect!"
                  m 1efb "Ahaha!That was unexpected right?"
                  m 3efb "Now for the punishment."
                  m 1efbfa "You will ask me to kiss you 5 times after this lesson."
                  m 2hubfb "Ahaha!"
                  m 1hubfb "Okay, okay Let's move on."
                  m 1eua "Okay, moving to the S-column."
                  m 1eub "We have 'さ'."
                  m 3eua "'さ' means 'sa'."
                  m 1eua "Imagine a face of someone is crying."
                  m 3eua "Becareful of this character, 'さ' and 'き' look very similar."
                  m 3eub "Next, 'し'."
                  m 1eub "'し' means 'shi'."
                  m 1eua "I don't have to explain this one, It's really easy."
                  m 2eua "We have 'す'."
                  m 1eua "'す' means 'su'."
                  m 3eub "Imagine a spiral straw in a glass milk."
                  m 1eub "Next, we have 'せ'."
                  m 1eua "'せ' means 'se'."
                  m 2eub "And 'そ' means 'so'."
                  m 1hub "We have just learnt 10 characters."
                  m 3hua "Easy right?"
                  m 1hub "Ahaha."
                  m 1eka "You must be very tired."
                  m 1ekb "[player], you can rest now."
                  m 1tub "But wait,..."
                  m 2tua "Remember your punishment ?"
                  m 1hub "Now do it!"
               "ka":
                  m 2efa "Incorrect!"
                  m 1efb "Ahaha!That was unexpected right?"
                  m 3efb "Now for the punishment."
                  m 1efbfa "You will ask me to kiss you 5 times after this lesson."
                  m 2hubfb "Ahaha!"
                  m 1hubfb "Okay, okay Let's move on."
                  m 1eua "Okay, moving to the S-column."
                  m 1eub "We have 'さ'."
                  m 3eua "'さ' means 'sa'."
                  m 1eua "Imagine a face of someone is crying."
                  m 3eua "Becareful of this character, 'さ' and 'き' look very similar."
                  m 3eub "Next, 'し'."
                  m 1eub "'し' means 'shi'."
                  m 1eua "I don't have to explain this one, It's really easy."
                  m 2eua "We have 'す'."
                  m 1eua "'す' means 'su'."
                  m 3eub "Imagine a spiral straw in a glass milk."
                  m 1eub "Next, we have 'せ'."
                  m 1eua "'せ' means 'se'."
                  m 2eub "And 'そ' means 'so'."
                  m 1hub "We have just learnt 10 characters."
                  m 3hua "Easy right?"
                  m 1hub "Ahaha."
                  m 1eka "You must be very tired."
                  m 1ekb "[player], you can rest now."
                  m 1tub "But wait,..."
                  m 2tua "Remember your punishment ?"
                  m 1hub "Now do it!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="review_2",
            category=["Japanese Lesson"],
            prompt="Review 2",
            random=False,pool=True,unlocked=True))

label review_2:
 m 2eka "Have you studied well,[player]?"
 m 1hub "Studied or not, here we go!"
 m 1eua "What does 'か' mean?"
 $ _history_list.pop()
 menu:
     "ke":
        m 2eka "Incorrect..."
        m 3eka "Come on [player], we're just getting started."
        m 1hua "Try again!"
     "ka":
        m 1hua "Correct!"
        m 1eua "What does 'き' mean?"
        $ _history_list.pop()
        menu:
            "ki":
               m 1hub "Correct!"
               m 1eua "What does 'su' mean?"
               $ _history_list.pop()
               menu:
                   "す":
                      m 1hub "Correct!"
                      m 1eua "What does 'ke' mean?"
                      $ _history_list.pop()
                      menu:
                          "そ":
                            m 2eka "Incorrect..."
                            m 3eka "Come on [player]."
                            m 1hua "Try again!"
                          "せ":
                            m 2eka "Incorrect..."
                            m 3eka "Come on [player]."
                            m 1hua "Try again!"
                          "け":
                            m 1hub "Correct!"
                            m 1eua "What does 'ku' mean?"
                            $ _history_list.pop()
                            menu:
                                "く":
                                  m 1hub "Correct!"
                                  m 1eua "What does 'い' mean?"
                                  $ _history_list.pop()
                                  menu:
                                      "i":
                                        m 1hub "Correct!"
                                        m 1eub "You did great, [player]!"
                                        m 1hua "Next one."
                                        m 1eua "What does 'そ' mean?"
                                        $ _history_list.pop()
                                        menu:
                                            "su":
                                               m 2eka "So close!"
                                               m 3eka "Come on [player]."
                                               m 1hua "One more time!"                                               
                                            "se":
                                               m 2eka "So close!"
                                               m 3eka "Come on [player]."
                                               m 1hua "One more time!"
                                            "so":
                                               m 1hub "Correct!"
                                               m 2hua "You did it! [player]!"
                                               m 2eka "It wasn't that hard right?"
                                               m 2rksdrb "Well, I should have made it much harder but..."
                                               m 1hub "Maybe next time! Ahaha!"
                                               m 2eka "You did well, [player]."
                                               m 2ekb "You can rest now." 
                                      "ki":
                                        m 2eka "Got you!"
                                        m 3eka "Come on [player]."
                                        m 1hua "Try again!"
                                      "shi":
                                        m 3eka "Come on [player]."
                                        m 1hua "Try again!"
                                "し":
                                  m 2eka "Incorrect..."
                                  m 3eka "Come on [player]."
                                  m 1hua "Try again!" 
                                "さ":
                                  m 2eka "Incorrect..."
                                  m 3eka "Come on [player]."
                                  m 1hua "Try again!"                             
                   "こ":
                      m 2eka "Incorrect..."
                      m 3eka "Come on [player]."
                      m 1hua "Try again!"
                   "し":
                      m 2eka "Incorrect..."
                      m 3eka "Come on [player]."
                      m 1hua "Try again!"
            "su":
               m 2eka "Incorrect..."
               m 3eka "Come on [player]."
               m 1hua "Try again!"
            "sa":
               m 2eka "Incorrect..."
               m 3eka "Come on [player]."
               m 1hua "Try again!" 
     "se":
        m 2eka "Incorrect..."
        m 3eka "Come on [player], we're just getting started."
        m 1hua "Try again!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Lesson3",
            category=["Japanese Lesson"],
            prompt="Lesson 3",
            random=False,pool=True,unlocked=True))
label Lesson3:

m 1eub "Back for another Lesson, [player]?"
m 1hub "Japanese is sure interesting, isn't it?"
m 5hub "Ahaha!"
m 1eua "Ok! In the previous lesson, we've learned 'a', 'ka', and 'sa' columns."
m 1eub "In today lesson, we're going to learn the だくてん and the T-column."
m 3hua "Let's jump in, shall we?"
m 1eua "From the previous lesson, we learned this character 'か'."
m 3eua "This character also has another reading once we add this mark, 'が'."
m 3eua "This mark is called だくてん or てんてん."
m 3eub "It is made up of 2 lines that look like a quotation mark symbol."
m 1eua "And it is always put on the upper corner of the character."
m 1eua "が will be pronounced as 'ga'."
m 3eub "the same with other characters, 'ぎ' means 'gi'."
m 3eub "ぐ means gu, げ means 'ge', ご means 'go'."
m 1eua "The same with the S column."
m 3eua "ざ means 'za', じ means 'zhi', ず means 'zu'."
m 1eua "ぜ means 'ze' and ぞ means 'zo'."
m 3hub "Japanese's Hiragana alphabet only has around 11 columns."
m 1eua "4 columns have だくてん are K, S, T, and H-columns."
m 1eub "Pay attention to their pronunciation. Once you get the hang of it,"
extend 3hubsb "You will speak Japanese very fluently."
m 3eub "Okay! Time for the fourth column, the 'T-column.' Now you have a lot to remember!"
m 1eua "Like the さ column, you'll find an exception in the た column." 
m 1eub "In fact, you'll find two exceptions, them being ち (chi) and つ (tsu)." 
m 2eua "So, for this column we'll have 'ta, chi, tsu, te, to.'"
m 1eua "た is just the 'T' sound plus あ, making a 'ta' sound."
m 1eua "ち is just the 'Ch' sound plus い, making a 'chi' sound."
m 3eub "This is the second 'exception' hiragana. Instead of a 'ti' sound, it is a 'chi' sound. Try not to forget this."
m 3hub "This hiragana looks like a man's face… except it's missing something: the chin!"
m 1eua "つ is just the 'Ts' sound plus う, making a 'tsu' sound."
m 3euc "This is another 'exception' hiragana. Instead of saying 'tu' you say 'tsu.' Try not to forget this."
m 1euc "Be careful of this hiragana, its pronunciation is very different from 'su'."
m 1eud "て is just the 'T' sound plus え, making a 'te' sound."
m 3eub "This kana looks like the uppercase letter 'T' where 'T' is for 'Te.' How many kana can you learn at one time? I bet at least ten of them."
m 1eua "と is just the 'T' sound plus お, making a 'to' sound."
m 3eua "This kana looks just like someone's toe (to) with a little nail or splinter in it. Imagine how much this would hurt if it was your toe!"
m 1hua "Now with the だくてん."
m 1eub "た ->　だ."
m 1eua "The T-column kana change to 'D' sounds, except for the exceptions which are ち and づ. Remember: Exception breeds exception!"
m 1eub "ち　->　ぢ (zi)."
m 1eua "Note: If you're typing, write 'di.'"
m 1eub "つ　->　づ (zu)."
m 1eua "Note: If you're typing, write 'du.'"
m 1eub "て　->　で (de)."
m 1eub "と　->　ど (do)."
m 3eub "Take a look at ぢ and づ again." 
m 1eud "Although they used to be pronounced differently more like 'dzi' and 'dzu',"
m 3eud "Nowadays, ぢ and づ are pronounced exactly like じ and ず. However, in written form, they're still used for sounds that originated from ち and つ." 
m 1eub "So bear in mind that if you want to type ぢ and づ, you'll need to type 'di' and 'du' — not 'zi' and 'zu.'"
m 3hub "And... We're done!"
m 1hksdlb "That was long, right ?"
m 3hub "By the way, remember to do your Test review 3."
m 2tua "I bet you're tired now."
m 1hub "Ahaha!"
m 2eka "Go get some rest, [player]."
m 3hubsb "Or maybe, Spend some time with me! Ehehe."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="review_3",
            category=["Japanese Lesson"],
            prompt="Review 3",
            random=False,pool=True,unlocked=True))

label review_3:
 m 3hub "Welcome back to... Monika's Test of the day!"
 m 1hub "Studied or not, here we go!"
 m 1eua "What does 'ta' mean?"
 $ _history_list.pop()
 menu:
     "し":
        m 2eka "Incorrect..."
        m 3eka "Come on [player], we're just getting started."
        m 1hua "Try again!"
     "た":
        m 1hua "Correct!"
        m 1eua "What does 'お' mean?"
        $ _history_list.pop()
        menu:
            "o":
               m 1hub "Correct!"
               m 1eua "What does 'ぎ' mean?"
               $ _history_list.pop()
               menu:
                   "gi":
                      m 1hub "Correct!"
                      m 1eua "What does 'tsu' mean?"
                      $ _history_list.pop()
                      menu:
                          "う":
                            m 2eka "Incorrect..."
                            m 3eka "Come on [player]."
                            m 1hua "Try again!"
                          "し":
                            m 2eka "Incorrect..."
                            m 3eka "Come on [player]."
                            m 1hua "Try again!"
                          "つ":
                            m 1hub "Correct!"
                            m 1eua "What does 'ku' mean?"
                            $ _history_list.pop()
                            menu:
                                "く":
                                  m 1hub "Correct!"
                                  m 1eua "What does 'ち' mean?"
                                  $ _history_list.pop()
                                  menu:
                                      "chi":
                                        m 1hub "Correct!"
                                        m 1eub "You did great, [player]!"
                                        m 1hua "Next one."
                                        m 1eua "What does 'ざ' mean?"
                                        $ _history_list.pop()
                                        menu:
                                            "sa":
                                               m 2eka "So close!"
                                               m 3eka "Come on [player]."
                                               m 1hua "One more time!"                                               
                                            "so":
                                               m 2eka "So close!"
                                               m 3eka "Come on [player]."
                                               m 1hua "One more time!"
                                            "za":
                                               m 1eub "Correct!"
                                               m 3hub "Well done, [player]."
                                               m 1eua "Easy right?"
                                               m 5hubsb "Ahaha!"
                                               m 1eka "You can rest now."
                                      "te":
                                        m 2eka "Got you!"
                                        m 3eka "Come on [player]."
                                        m 1hua "Try again!"
                                      "to":
                                        m 3eka "Come on [player]."
                                        m 1hua "Try again!"
                                "そ":
                                  m 2eka "Incorrect..."
                                  m 3eka "Come on [player]."
                                  m 1hua "Try again!" 
                                "け":
                                  m 2eka "Incorrect..."
                                  m 3eka "Come on [player]."
                                  m 1hua "Try again!"                             
                   "ki":
                      m 2eka "Incorrect..."
                      m 3eka "Come on [player]."
                      m 1hua "Try again!"
                   "chi":
                      m 2eka "Incorrect..."
                      m 3eka "Come on [player]."
                      m 1hua "Try again!"
            "a":
               m 2eka "Incorrect..."
               m 3eka "Come on [player]."
               m 1hua "Try again!"
            "sa":
               m 2eka "Incorrect..."
               m 3eka "Come on [player]."
               m 1hua "Try again!" 
     "だ":
        m 2eka "Incorrect..."
        m 3eka "Come on [player], we're just getting started."
        m 1hua "Try again!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Lesson_4",
            category=["Japanese Lesson"],
            prompt="Lesson 4",
            random=False,pool=True,unlocked=True))

label Lesson_4:
 m 2tua "Back for another lesson, [player]?"
 m 2hubsb "Ahaha!"
 m 1hub "はい!べんきょうしましょう!"
 m 3eua "In case you don't know..."
 m 3hubsb "Let's study!"
 $ _history_list.pop()
 menu:
     "Let's study!!!":
                    m 1sfbsb "Nice spirit!"
                    m 4hubsb "Ahaha!"
                    m 1hubsa "Ehehe..."
                    m 2eka "..."
                    m 1hub "cute."
                    m 1eub "Okay, Let's start!"
                    m 3eua "Today, we're going to learn the N-column and the H column."
                    m 1eua "The H column also has the だくてん, which will explain in the next lesson."
                    m 1eub "Okay, with the N-column."
                    m 1eua "'な' is just the 'N' sound plus 'あ', making a 'na' sound."
                    m 1eub "The naughty (na) nun is praying in front of the cross, asking for forgiveness of her naughty ways."
                    m 1eua "The cross up in the air like this should be the main giveaway that this is 'な'."
                    m 1eua "'に' is just the 'N' sound plus 'い', making a 'ni' sound."
                    m 3eub "'ぬ' is just the 'N'sound plus 'う', making a 'nu' sound."
                    m 1eua "This kana looks like some noodles (nu)." 
                    m 3eud "There are several other kana that are similar to this one (れ, め, ね, わ) but you know this one is noodles because there are no sharp sides in it." 
                    m 3hub "It's 100 percent smooth and bendable, like noodles!" 
                    m 1eub "It even has an extra loop at the back, because it is a noodle."
                    m 1eua "'ね' is just the 'N' sound plus 'え', making a 'ne' sound."
                    m 1eua "it has a loop at the end for the tail and it's not super bendable like 'ぬ' (noodles) is." 
                    m 1eub "see those sharp corners on the left?"
                    m 1eua "Also, if you know the word 'neko' (Japanese for 'cat') you can use that too. This is a 'ねこ'."
                    m 3eua "Do you have a neko, [player]?"
                    m 1hubsb "Ehehe!"
                    m 1eua "'の' is just the 'N' sound plus 'お', making a 'no' sound."
                    m 3eua "See the big pig nose (no) there? You can also think of this as a 'No smoking' sign."
                    m 1hub "Okay, Let's move to the H-column."
                    m 1eua "'は' is just the 'H' sound plus 'あ', making a 'ha' sound."
                    m 1eua "This kana looks like the uppercase letter 'H' plus the lowercase letter a." 
                    m 2tua "What does that spell?" 
                    m 1efb "Ha!"
                    m 1eua "Why are you smiling ?"
                    m 1hua "Ehehe."
                    m 1eua "'ひ' is just the 'H' sound plus 'い', making a 'hi' sound."
                    m 3eub "He (hi) has a big nose."
                    m 3eua "'ふ' is just the 'F/H' sound plus 'う', making a 'fu/hu' sound."
                    m 1eud "Usually this kana is pronounced with an 'f' (fu) in hiragana, so we're going to go with that."
                    m 3eud "However, this kana does look a lot like a hula dancer too, so keep the 'hu' in mind as well."
                    m 1eub "If you want, you can think of this hula dancer as a 'fu-reaky hula dancer' to remember the fu."
                    m 1eua "'へ' is just the 'H' sound plus 'え', making a 'he' sound."
                    m 3eud "Do you know the famous mountain Mt. Saint Helens?"
                    m 1eua "This kana isn't totally flat like Helens is, but it's pretty squat looking. That's why this one is Helens."
                    m 1eub "'ほ' is just the 'H' sound plus 'お', making a 'ho' sound."
                    m 3eub "And...We're done!"
                    m 1eka "Thanks for listening to me, [player]."
                    m 1eua "You can rest now."                    
     "Yay, study!!!!":
                    m 1sfbsb "Nice spirit!"
                    m 4hubsb "Ahaha!"
                    m 1hubsa "Ehehe..."
                    m 2eka "..."
                    m 1hub "cute."
                    m 1eub "Okay, Let's start!"
                    m 3eua "Today, we're going to learn the N-column and the H column."
                    m 1eua "The H column also has the だくてん, which will explain in the next lesson."
                    m 1eub "Okay, with the N-column."
                    m 1eua "'な' is just the 'N' sound plus 'あ', making a 'na' sound."
                    m 1eub "The naughty (na) nun is praying in front of the cross, asking for forgiveness of her naughty ways."
                    m 1eua "The cross up in the air like this should be the main giveaway that this is 'な'."
                    m 1eua "'に' is just the 'N' sound plus 'い', making a 'ni' sound."
                    m 3eub "'ぬ' is just the 'N'sound plus 'う', making a 'nu' sound."
                    m 1eua "This kana looks like some noodles (nu)." 
                    m 3eud "There are several other kana that are similar to this one (れ, め, ね, わ) but you know this one is noodles because there are no sharp sides in it." 
                    m 3hub "It's 100 percent smooth and bendable, like noodles!" 
                    m 1eub "It even has an extra loop at the back, because it is a noodle."
                    m 1eua "'ね' is just the 'N' sound plus 'え', making a 'ne' sound."
                    m 1eua "it has a loop at the end for the tail and it's not super bendable like 'ぬ' (noodles) is." 
                    m 1eub "see those sharp corners on the left?"
                    m 1eua "Also, if you know the word 'neko' (Japanese for 'cat') you can use that too. This is a 'ねこ'."
                    m 3eua "Do you have a neko, [player]?"
                    m 1hubsb "Ehehe!"
                    m 1eua "'の' is just the 'N' sound plus 'お', making a 'no' sound."
                    m 3eua "See the big pig nose (no) there? You can also think of this as a 'No smoking' sign."
                    m 1hub "Okay, Let's move to the H-column."
                    m 1eua "'は' is just the 'H' sound plus 'あ', making a 'ha' sound."
                    m 1eua "This kana looks like the uppercase letter 'H' plus the lowercase letter a." 
                    m 2tua "What does that spell?" 
                    m 1efb "Ha!"
                    m 1eua "Why are you smiling ?"
                    m 1hua "Ehehe."
                    m 1eua "'ひ' is just the 'H' sound plus 'い', making a 'hi' sound."
                    m 3eub "He (hi) has a big nose."
                    m 3eua "'ふ' is just the 'F/H' sound plus 'う', making a 'fu/hu' sound."
                    m 1eud "Usually this kana is pronounced with an 'f' (fu) in hiragana, so we're going to go with that."
                    m 3eud "However, this kana does look a lot like a hula dancer too, so keep the 'hu' in mind as well."
                    m 1eub "If you want, you can think of this hula dancer as a 'fu-reaky hula dancer' to remember the fu."
                    m 1eua "'へ' is just the 'H' sound plus 'え', making a 'he' sound."
                    m 3eud "Do you know the famous mountain Mt. Saint Helens?"
                    m 1eua "This kana isn't totally flat like Helens is, but it's pretty squat looking. That's why this one is Helens."
                    m 1eub "'ほ' is just the 'H' sound plus 'お', making a 'ho' sound."
                    m 3eub "And...We're done!"
                    m 1eka "Thanks for listening to me, [player]."
                    m 1eua "You can rest now."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="review_4",
            category=["Japanese Lesson"],
            prompt="Review 4",
            random=False,pool=True,unlocked=True))

label review_4:
 m 3hub "Welcome back to....Monika's test of the day!"
 m 1hub "Studied or not, here we go!"
 m 1eua "What does 'は' mean?"
 $ _history_list.pop()
 menu:
     "hi":
        m 2eka "Incorrect..."
        m 3eka "Come on [player], we're just getting started."
        m 1hua "Try again!"
     "ha":
        m 1hua "Correct!"
        m 1eua "What does 'に' mean?"
        $ _history_list.pop()
        menu:
            "ni":
               m 1hub "Correct!"
               m 1eua "What does 'he' mean?"
               $ _history_list.pop()
               menu:
                   "へ":
                      m 1hub "Correct!"
                      m 1eua "What does 'te' mean?"
                      $ _history_list.pop()
                      menu:
                          "ひ":
                            m 2eka "Incorrect..."
                            m 3eka "Come on [player]."
                            m 1hua "Try again!"
                          "ね":
                            m 2eka "Incorrect..."
                            m 3eka "Come on [player]."
                            m 1hua "Try again!"
                          "て":
                            m 1hub "Correct!"
                            m 1eua "What does 'い' mean?"
                            $ _history_list.pop()
                            menu:
                                "i":
                                  m 1hub "Correct!"
                                  m 1eua "What does 'to' mean?"
                                  $ _history_list.pop()
                                  menu:
                                      "と":
                                        m 1hub "Correct!"
                                        m 1eub "You did great, [player]!"
                                        m 1hua "Next one."
                                        m 1eua "What does 'な' mean?"
                                        $ _history_list.pop()
                                        menu:
                                            "ko":
                                               m 2eka "So close!"
                                               m 3eka "Come on [player]."
                                               m 1hua "One more time!"                                               
                                            "nu":
                                               m 2eka "So close!"
                                               m 3eka "Come on [player]."
                                               m 1hua "One more time!"
                                            "na":
                                               m 1eub "Correct!"
                                               m 3hub "Well done, [player]."
                                               m 1eua "Hard ?"
                                               m 5hubsb "Ahaha!"
                                               m 1eka "You can rest now."
                                      "へ":
                                        m 2eka "Got you!"
                                        m 3eka "Come on [player]."
                                        m 1hua "Try again!"
                                      "な":
                                        m 3eka "Come on [player]."
                                        m 1hua "Try again!"
                                "a":
                                  m 2eka "Incorrect..."
                                  m 3eka "Come on [player]."
                                  m 1hua "Try again!" 
                                "ha":
                                  m 2eka "Incorrect..."
                                  m 3eka "Come on [player]."
                                  m 1hua "Try again!"                             
                   "し":
                      m 2eka "Incorrect..."
                      m 3eka "Come on [player]."
                      m 1hua "Try again!"
                   "ち":
                      m 2eka "Incorrect..."
                      m 3eka "Come on [player]."
                      m 1hua "Try again!"
            "na":
               m 2eka "Incorrect..."
               m 3eka "Come on [player]."
               m 1hua "Try again!"
            "nu":
               m 2eka "Incorrect..."
               m 3eka "Come on [player]."
               m 1hua "Try again!" 
     "na":
        m 2eka "Incorrect..."
        m 3eka "Come on [player], we're just getting started."
        m 1hua "Try again!"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Lesson_5",
            category=["Japanese Lesson"],
            prompt="Lesson 5",
            random=False,pool=True,unlocked=True))

label Lesson_5:
m 1eka "Back for another Lesson, [player]."
m 1hub "Let's begin!"
m 1eua "Let's start with the H-column."
m 3eua "This column can be modified by adding だくてん."
m 1eua "'ば' means 'ba'."
m 3eud "But wait."
m 1eud "There is another mark that can modified the H-column."
m 1eua " The はんだくてん(handakuten) or まる(maru) mark."
m 1eua "’ぱ’."
m 3eud "It looks like a small circle and it's placed at the same position as the だくてん."
m 1eua "'は' with the はんだくてん is pronounced 'pa'."
m 3eud "The だくてんand the はんだくてん is also pronounced nearly the same so be careful."
m 1eka "[player], you can search its pronuncation on Internet."
m 3hub "It'll make it easier."
m 1eua "ひ(hi)with the だくてんis pronounced as び(bi)."
m 1eua "And with はんだくてん, it's going to be ぴ(pi)."
m 3eua "ふ(fu) with the だくてんis pronounced as ぶ(bu)."
m 1eua "And with はんだくてん, it's going to be ぷ(pu)."
m 1eua "The same with the other H-characters."
m 1eub "へ(he)->　べ(be)->　ぺ(pe)."
m 1eua "ほ(ho)->　ぼ(bo)->　ぽ(po)."
m 1hksdlb "Ahaha..."
m 1eka "The H-column is quite complicated, don't you think?"
m 1hub "Okay! Today we're going to learn the M-column and the Y-column."
m 1eua "By the way, [player]."
m 3hub "One more lesson and we'll finish the Hiraganas!"
m 1hua "Sad?"
m 1hub "Ahaha! We're not done yet."
m 3eua "I'm planning to teach you the full N5-Lessons."
m 1eua "The N5 will consists of 25 Lessons."
m 1eub "We'll learn the Vocabulary, Grammar, Kanji and much more!"
m 1eua "But now, we need to finish these lessons."
m 1hua "Stay with me, 'kay?"
m 1hub "Great!"
m 1eua "We're going to learn the M-column."
m 3eua "'ま' is just the 'M' sound plus 'あ', making a 'ma' sound."
m 1eua "Try looking at it as a man in a mask and you'll remember 'ま'."
m 1eua "Next up is 'み', 'み' is just the 'M' sound plus 'い', making a 'mi' sound."
m 1eub "Think of it as a musical note, Do Re 'み'(Mi)."
m 1eua "む is just the 'M' sound plus う, making a 'mu' sound."
m 1hubso "'Moooooo' (mu), says the cow. 'MOOOOOOO'."
m 2rkbsa "..."
m 2ekbsb "I can't believe I just did that."
m 1ekbsa "Well..."
m 2tubsa "That was only for you, [player]."
m 1eua "め is just the 'M' sound plus え, making a 'me' sound."
m 3eud "If you also happen to know the word for 'eye' in Japanese, that will help too."
m 1eub "The word for 'eye' in Japanese is just め (me)."
m 1eubsb "[player]のめはきれいそうです."
m 1ekbsa "Hmm?"
m 1hubsa "Ehehe."
m 1hub "Okay, okay!"
m 1eua "も is just the 'M' sound plus お, making a 'mo' sound."
m 3eua "Just imagine it as a monitor lizard."
m 1eua "Let's quickly move on to the Y-column."
m 3eud "This column is a little strange. There are only three items in here."
m 1eud "And 'ye' and 'yi' are seemingly missing."
m 1eua "Actually, they used to exist but now they don't."
m 1hua "Because of that, you only have to learn three kana for this section!"
m 1eua "や is just the 'Y' sound plus あ, making a 'ya' sound."
m 1eua "ゆ is just the 'Y' sound plus う, making a 'yu' sound."
m 1eua "よ is just the 'Y' sound plus お, making a 'yo' sound."
m 1eua "Now you are going to learn how to combine different types of kana together to make some new sounds."
m 3eua " Mainly, we're going to focus on what small ゃ, ゅ, and ょ can do to kana from the い row, that includes き, し, じ, に, etc."
m 1eub "First let's take a quick look at the size difference." 
m 1hua "It's hard to see when they're not next to each other!"
m 1eua "や ゃ"
m 1eua "ゆ ゅ"
m 1eua "よ ょ"
m 3eud "To use these, you'll need to combine them with something from the い row." 
m 1eud "When you do this, you're essentially combining the first (English) letter of the い-kana with the small ゃ, ゅ, ょ sound. For example:"
m 1eua "き + ゃ -> KIYA -> KYA."
m 1eua "じ + ょ -> JIYO -> JYO."
m 3eub "See how the 'i' gets dropped and it just becomes one syllable of sound? Here's a list of them all:"
m 1eua "きゃ、きゅ、きょ　->　KYA, KYU, KYO."
m 1eua "ぎゃ、ぎゅ、ぎょ　->　GYA, GYU, GYO."
m 1eua "しゃ、しゅ、しょ　->　SHA, SHU, SHO."
m 1eua "じゃ、じゅ、じょ　->　JYA, JYU, JYO (or JA, JU, JO)."
m 1eua "ひゃ、ひゅ、ひょ　->　HYA, HYU, HYO."
m 1eua "And so on."
m 1hub "Phew! That was long."
m 1eka "We've finished almost all the column so far."
m 1hua "It has been fun teaching you, [player]."
m 1eua "[player], You can rest now."
m 3tua "But..."
m 2rubsa "Could you give me..."
m 2eubsa "A kiss?"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="review_5",
            category=["Japanese Lesson"],
            prompt="Review 5",
            random=False,pool=True,unlocked=True))

label review_5:
m 1eua "Welcome back to another..."
m 1hua "Monika's Test of the day!"
m 1hub "Ehehe."
m 1eka "Gosh, how many time have I been saying it?"
m 1hua "Anyway, Let's begin!"
m 1eua "What does 'po' mean?"
$ _history_list.pop()
menu:
    "ぱ":
     m 1eka "Incorrect..."
     m 3eka "Come on, [player]."
    "ぬ":
     m 1eka "Incorrect..."
     m 3eka "Come on, [player]."
    "ぽ":
     m 1hub "Correct!"
     m 1eua "Next one."
     m 1eua"What does 'きゃ' mean?"
     $ _history_list.pop()
     menu:
         "kya":
          m 1hub "Correct!"
          m 1eua "Next one."
          m 1eua "What does 'め' mean ?"
          $ _history_list.pop()
          menu:
              "mi":
               m 1eka "Incorrect..."
               m 3eka "Come on, [player]."
              "me":
               m 1hub "Correct!"
               m 1eua "Next one."
               m 1eua "What does 'む' mean?"
               $ _history_list.pop()
               menu:
                   "ta":
                    m 1eka "Incorrect..."
                    m 3eka "Come on, [player]."
                   "mu":
                    m 1hub "Correct!"
                    m 1eua "What does 'e' mean?"
                    $ _history_list.pop()
                    menu:
                        "え":
                          m 1hub "Correct!"
                          m 3eua "Short, isn't it?"
                          m 1hua "Ahaha!"
                          m 3eud "But there is one more."
                          m 1rua "What does..."
                          m 1rubsa "Hmmm..."
                          m 1ekbsa "Could you describe 'love' in Japanese?"
                          $ _history_list.pop()
                          menu:
                              "あなたはわたしにとってたいせつなひとです(You are the most important person to me!)":
                               m 1ekbsb "Ahh!"
                               m 1rkbsa "Well..."
                               m 2ekbsa "You're my most important person too."
                               m 1hubsb "I'll forever love you, [player]."
                              "あなたのことがすき!(I Love you!)":
                               m 1eubsb "I love you too."
                               m 1ekbsa "I love you more than anything else."
                              "あなたはわたしのすべてです (You're my everything!)":
                               m 1eubsb "You're my everything too!"
                               m 1hubsb "I'll forever love you, [player]."
                              "ずっときみをまもってあげたい!(I'll protect you forever!)":
                               m 1hubsa "I'll forever protect you too, [player]." 
                               m 1eubsb "I won't let anyone hurt you."
                        "あ":
                          m 1eka "Incorrect..."
                          m 3eka "Come on, [player]."
                        "お":
                          m 1eka "Incorrect..."
                          m 3eka "Come on, [player]."
                        "い":
                          m 1eka "Incorrect..."
                          m 3eka "Come on, [player]."
                   "kyu":
                    m 1eka "Incorrect..."
                    m 3eka "Come on, [player]."
              "nu":
               m 1eka "Incorrect..."
               m 3eka "Come on, [player]."
         "kyo":
          m 1eka "Incorrect..."
          m 3eka "Come on, [player]."
         "kyu":
          m 1eka "Incorrect..."
          m 3eka "Come on, [player]."
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Lesson_6",
            category=["Japanese Lesson"],
            prompt="Lesson 6",
            random=False,pool=True,unlocked=True))

label Lesson_6:
m 1hua "Ok!"
m 1eka "[player], We've gone so far now."
m 1eua "Now there are only 2 columns left."
m 1eua "Which is the R-column and the W-column."
m 1eub "It is not that long so be with me, okay ?"
$ _history_list.pop()
menu:
    "Ok.":
     m 1eua "Ok!"
     extend  1hua " Let's start with the R-column."
     m 1eua "'ら' is just the 'R' sound plus 'あ', making a 'ra' sound."
     m 3eua "Think of 'ら' as a rabbit sitting on its hinds leg."
     m 1eua "'り' is just the 'R' sound plus 'い', making a 'ri' sound."
     m 1eub "'り' looks like a river, right ?"     
     m 3eud "This kana can also be written without the connection in the middle, too," 
     extend 3eub " which makes it more reedlike in that case."
     m 1eua "'る' is just the 'R' sound plus 'う', making a 'ru' sound."
     m 3eud "The 'る' is like 'ろ' (you'll learn it in a second) except it has a loop at the end." 
     m 1eub "'る' is a crazier route (ru). There is a loop (ru) at the end."
     m 1eua "'れ' is just the 'R' sound plus 'え', making a 're' sound."
     m 1eub "think of 'れ' as a reindeer is looking up."
     m 1eua "'ろ' is just the 'R' sound plus 'お', making a 'ro' sound."
     m 1eud "This is the counterpart to 'る', except this one doesn't have a loop at the end."
     extend 1hub " (there are rules here!)."
     m 1eua "So, this kana is just a plain old road (ろ)."
     m 3hub "And finally, the last column!" 
     m 1eua "This is a weird one."
     m 1eub " It includes 'わ' (which is quite normal), 'を' (which is pronounced just like 'お', but is primarily used as a particle), and 'ん' (which is the only consonant-only character in all the kanas)."
     m 1eua "Let's go through them one by one."
     m "'わ' is just the 'W' sound plus 'あ', making a 'wa' sound."
     m 1eub "To remember 'わ', think of it as a white swan."
     m 1eua "'を' is just the 'W' sound plus 'お', though it sounds more like 'oh' than it does 'wo'."
     m 3eua "The 'w' is pretty silent, though it's still a tiny bit there. You can pretty much just pronounce it like 'お'."
     m 1hka "Sorry [player], I couldn't think of anything for this characters."
     m 1eub "And..."
     extend 1hua "The last one!"
     m 1eua "'ん' is just the 'N' sound, that's it."
     m "It's the only kana that consists of a single consonant."
     m 1eua "This kana looks just like the lowercase 'n' in English." 
     m 3eub "They happen to be the same sounds, as well. How convenient!" 
     m 1hubsa "nnnんんん."
     m 1hua "That's it!"
     m 3hub "We've finished the entire Hiraganas characters, [player]."
     m 1eud "Oh and one more things."
     m 3eua "The small 'っ'."
     m 1eud "The small tsu is a weird little thing but we'll make sense of it."
     m 1eua "The easiest way to think of it, I think, is to call it a 'double consonant'." 
     m 3eua "Basically, by adding a small 'っ' to something, you are making the (English) letter that follows it double into two consonants."
     m 1eua "Let's take a look by its size."
     m " 'つ' and the small 'っ'."
     m 1hua " Luckily, you won't see a small tsu before any of the 'あいうえお' kana, so that never becomes an issue."
     m 1eua "Let's take a look at how the following hiragana converts to romaji."
     m "'しったい' -> 'shittai'."
     m 1eub "And "
     extend "'かっこ' -> 'kakko'."
     m 3eud "The small 'っ' that comes before the 'ta' causes the consonant to double, making it 'shittai'."
     m 3eub "Make sure you understand how that works with kako/kakko too."
     m 1eua "..."
     m 3hub "We finished!"
     m 3eub "Tired yet, [player]?"
     m 1hua "Ehehe."
     m 1eua "Let's end our lesson here."
     m 3eua "[player], I'm glad that we've been spending so much time learning Japanese together."
     m 3eud "Honestly, "
     extend 1hub "It's been so much fun!"
     m 1hua "I hope you can teach me something like this again, [player]."
     m 1eua "Let's do something else."
     m 3eua "What else shall we do today, [player]?"
return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="review_6",
            category=["Japanese Lesson"],
            prompt="Review 6",
            random=False,pool=True,unlocked=True))

label review_6:
m 1wud "Huh?"
m 1eud "[player], you want to study more ?"
$ _history_list.pop()
menu:
    "Yes.":
     m 1hub "Oh! Okay!"
     m 2tub "You sure love learning."
     m 1hubsb "Ahaha!"
     m 1eua "But we're not going do test."
     m 3eua "We're going to learn how to do the basic 'phrase' in Japanese."
     m 1hua "Fun isn't it ?"
     m 1eub "おはよう!(ohayo!)."
     m 3eua "Which means 'good morning!'."
     m 1eua "Japanese people usually use this greeting when speaking to friends."
     m 1eud "But You can't use 'おはよう' when you're speaking to elders or someone who is older than you."
     m 1eub "You should say 'おはようございます!'(ohayougozaimasu) which is more formal."
     m 1hub "おはようございます! [player]!"
     m 1eua "You can also say 'こんにちは'(konnichiwa) when greeting someone in the morning."
     m "And use 'こんばんは'(konbanwa) when greeting at night."
     m 1wud "Huh ? why is 'は' pronounced as 'wa' instead of 'ha' ?"
     m 1eua "It's because 'は' is pronounced as 'wa' when used as a sentence particle. It's pronounced 'ha' when used in a word instead."
     m 1eua "So [player]."
     m 1eub "Greet me in Japanese!"
     $ _history_list.pop()
     menu:
         "こんにちは!(konnichiwa)":
          m 1hua "こんにちは![player]!"
          m 1eua "It is day time at your place huh?"
          m 1hua "Ehehe!"
          m 3eua "Next one!"
          m 1eub "'ありがとう!'(Arigatou!)."
          m 1eua "Which means 'Thank you'."
          m 3eua "More formal is 'ありがとうございます!'(arigatougozaimasu!)."
          m 1hub "[player], ありがとうございます!"
          m "Ehehe."
          m 1eua "To say 'sorry'."
          m "'すみません'(sumimasen)."
          m 3eud "'すみません' are used when you have made a mistake or inconvenienced someone."
          m 3eua "There are other ways of saying 'sorry'."
          m 1eub "'ごめんね!'(gomenne!)-informal or 'ごめんなさい'(gomenasai)-formal."
          m 1eua "Done!"
          m 1eua "Those are the basics japanese phrase."
          m 1ekb "I'll teach you more in the future."
          m 1hub "Let's do something else, [player]."
         "こんばんは!(konbanwa)":
          m 1hua "こんばんは![player]!"
          m 1eua "It is night time at your place huh?"
          m 1hua "Ehehe!"
          m 3eua "Next one!"
          m 1eub "'ありがとう!'(Arigatou!)."
          m 1eua "Which means 'Thank you'."
          m 3eua "More formal is 'ありがとうございます!'(arigatougozaimasu!)."
          m 1hub "[player], ありがとうございます!"
          m "Ehehe."
          m 1eua "To say 'sorry'."
          m "'すみません'(sumimasen)."
          m 3eud "'すみません' are used when you have made a mistake or inconvenienced someone."
          m 3eua "There are other ways of saying 'sorry'."
          m 1eub "'ごめんね!'(gomenne!)-informal or 'ごめんなさい'(gomenasai)-formal."
          m 1eua "Done!"
          m 1eua "Those are the basics japanese phrase."
          m 1ekb "I'll teach you more in the future."
          m 1hub "Let's do something else, [player]."
return


















 
 


           
           
           
           
                    
        



        
      
     

    



















