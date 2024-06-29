# SemEval-2025 Task 12 : Bridging the Gap in Text-Based Emotion Detection

## Overview

Emotion detection is an important task in Natural Language Processing (NLP) that various applications such as building dialogue systems, opinion mining, and mental health analysis benefit from. However, most work on emotion detection has focused on high-resource languages. This shared task aims to reduce this gap by introducing new manually annotated emotion datasets for more than 30 predominantly low-resource languages from Africa, Asia, Eastern Europe, Latin America, along with a few high-resource languages.

## Tracks

Participants are asked to participate in one or more of the following tracks:

### Track 1: Multi-label Emotion Detection

Given a set of labeled training data in a target language, predict one or more emotions that the speaker is likely feeling in the text from the following emotion classes and neutral: Joy, Sadness, Fear, Anger, Surprise, Disgust, or Neutral.

### Track 2: Emotion Intensity (ordinal)

Given a set of labeled training data in a target language annotated with emotion, classify the text into one of four ordinal classes of intensity that best represents the emotional state of the writer:
1. No emotion
2. A low amount of emotion
3. A moderate amount of emotion
4. A high amount of emotion

### Track 3: Cross-lingual Emotion Detection

Given training and validation data in English, predict the emotion of a new text instance in a different target language from the set of six emotion classes: Joy, Sadness, Fear, Anger, Surprise, Disgust, or classified as Neutral.

## Languages

The shared task includes the following languages:

- **Africa**: Afrikaans, Algerian Arabic, Amharic, Hausa, Igbo, Kinyarwanda, Moroccan Arabic, Mozambican Portuguese, Nigerian-Pidgin, Oromo, Setswana, Somali, Swahili, Tigrinya, Twi, Xitsonga, isiXhosa, Yoruba, isiZulu
- **Asia**: Arabic, Chinese, Hindi, Indonesian, Javanese, Marathi
- **Europe & North America**: English, German, Romanian, Russian, Spanish, Tatar, Ukrainian
- **Latin America**: Brazilian Portuguese


## Dataset Structure

The dataset structure will vary depending on the track:

- **Track 1**: [Example Text, Joy, Sadness, Fear, Anger, Surprise, Disgust, Neutral]
- **Track 2**: [Example Text, 0,1,2,4]
- **Track 3**: [Example Text, Joy, Sadness, Fear, Anger, Surprise, Disgust, Neutral]

## Evaluation

The performance of each submission will be evaluated using F1-score based on the predicted labels and the gold ones. Participants will be provided with an evaluation script and a starter kit that includes a simple baseline.

## Organizers

| Organizers                   | Affiliation                 | Role              | Languages                                |
|------------------------------|-----------------------------|-------------------|------------------------------------------|
| Shamsuddeen Hassan Muhammad  | Imperial College London     | Lead Organizer    | hau, ibo, yor, pcm, twi, swa, ary, por, kin, zul, xho |
| Idris Abdulmumin             | University of Pretoria      | Co-Organizer      |                                          |
| Ibrahim Said Ahmad           | Northeastern University     | Co-Organizer      |                                          |
| David Ifeoluwa Adelani       | University College London   | Co-Organizer      |                                          |
| Seid Muhie Yimam             | Universität Hamburg         | Co-Organizer      | amh, orm, tig, som                       |
| Abinew Ali Ayele             | Universität Hamburg         | Co-Organizer      |                                          |
| Tadesse Destaw Belay         | IPN, Mexico                 | Co-Organizer      |                                          |
| Nedjma Ousidhoum             | Cardiff University          | Co-Organizer      | arb, arq                                 |
| Daniela Teodorescu           | University of Alberta       | Co-Organizer      | eng, ron                                 |
| Jan Philip Wahle             | University of Göttingen     | Co-Organizer      | deu, por                                 |
| Terry Ruas                   | University of Göttingen     | Co-Organizer      |                                          |
| Nirmal Surange               | IIIT Hyderabad              | Co-Organizer      | hin, mar                                 |
| Alham Fikri Aji              | MBZUAI                      | Co-Organizer      | ind, jav                                 |
| Yi Zhou                      | Cardiff University          | Co-Organizer      | zho                                      |
| Alexander Panchenko          | Skoltech                    | Co-Organizer      | rus, tat                                 |
| Vladimir Araujo              | KU Leuven                   | Co-Organizer      | esp                                      |
| Vukosi Marivate              | University of Pretoria      | Co-Organizer      | tsn, tso                                 |
| Saif M. Mohammad             | NRC Canada                  | Advisory Organizer| eng                                      |

## How to Participate

1. **Register**: Sign up on the competition platform (link to be provided).
2. **Download**: Access the datasets and starter kit from the repository.
3. **Develop**: Build your models using the provided data and baseline.
4. **Submit**: Upload your predictions to the evaluation server.
5. **Evaluate**: Receive feedback on your submission's performance.

## Ethical Considerations

This task will respect existing intellectual property by only making use of publicly and freely available datasets. Additionally, we adhere to the fifty ethical considerations in emotion recognition and the ACL Code of Ethics. The datasets will be approved by our respective Institutional Research Ethics Boards. Annotators will be paid the minimum wage of their respective countries (or higher), and their privacy will be respected.

## References

- [Findings of the WMT’22 shared task on large-scale machine translation evaluation for African languages](https://aclanthology.org/2022.wmt-1.72)
- [SemEval-2019 task 3: EmoContext contextual emotion detection in text](https://doi.org/10.18653/v1/S19-2005)
- [SemEval-2018 task 1: Affect in tweets](https://doi.org/10.18653/v1/S18-1001)
- [Textual emotion detection in health: Advances and applications](http://arxiv.org/abs/2109.08256)
