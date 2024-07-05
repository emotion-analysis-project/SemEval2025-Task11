# 🤗😲  SemEval-2025 Task 11 : Bridging the Gap in Text-Based Emotion Detection 😔😱😡😲🤮

- [Overview](#overview)
- [Languages](#languages)
- [Tracks](#tracks)
  - [Track A: Multi-label Emotion Detection](#track-a-multi-label-emotion-detection)
  - [Track B: Emotion Intensity (ordinal)](#track-b-emotion-intensity-ordinal)
  - [Track C: Cross-lingual Emotion Detection](#track-c-cross-lingual-emotion-detection)
- [Dataset Structure](#dataset-structure)
- [Evaluation](#evaluation)
- [Important Dates](#important-dates)
- [How to Participate](#how-to-participate)
- [Organizers](#organizers)
- [Competition Rules and Terms](#competition-rules-and-terms)
- [Resources](#resources)

## Overview

Emotion detection is an important task in Natural Language Processing (NLP) that various applications such as building dialogue systems, opinion mining, and mental health analysis benefit from. However, most work on emotion detection has focused on high-resource languages. This shared task aims to reduce this gap by introducing new manually annotated emotion datasets for more than 30 predominantly low-resource languages from Africa, Asia, Eastern Europe, Latin America, along with a few high-resource languages.


## Languages

The shared task includes the following languages:

- **Africa**: Afrikaans, Algerian Arabic, [Amharic](https://en.wikipedia.org/wiki/Amharic), Hausa, Igbo, Kinyarwanda, Moroccan Arabic, Mozambican Portuguese, Nigerian-Pidgin, Oromo, Setswana, Somali, Swahili, Tigrinya, Twi, Xitsonga, isiXhosa, Yoruba, isiZulu
- **Asia**: Arabic, Chinese, Hindi, Indonesian, Javanese, Marathi
- **Europe & North America**: English, German, Romanian, Russian, Spanish, Tatar, Ukrainian
- **Latin America**: Brazilian Portuguese


## Tracks

Participants can participate in one or more of the following tracks:


- **Track A: Multi-label Emotion Detection**: Given a set of labeled training data in a target language, predict one or more emotions that the speaker is likely feeling in the text from the following emotion classes and neutral: Joy, Sadness, Fear, Anger, Surprise, Disgust, or Neutral.

- **Track B: Emotion Intensity (ordinal)**: Given a set of labeled training data in a target language annotated with emotion, classify the text into one of four ordinal classes of intensity that best represents the emotional state of the writer:
(1) No emotion, (2),  A low amount of emotion (3) A moderate amount of emotion (4) A high amount of emotion

- **Track C: Cross-lingual Emotion Detection**: Given training and validation data in English, predict the emotion of a new text instance in a different target language from the set of six emotion classes: Joy, Sadness, Fear, Anger, Surprise, Disgust, or classified as Neutral.


## Dataset Structure

The dataset structure will vary depending on the track:

- **Track 1**: [Example Text, Joy, Sadness, Fear, Anger, Surprise, Disgust, Neutral]
- **Track 2**: [Example Text, 0,1,2,4]
- **Track 3**: [Example Text, Joy, Sadness, Fear, Anger, Surprise, Disgust, Neutral]

We provide the pilot dataset in the following folders: [Track A](#), [Track B](#), [Track C](#)

## Evaluation

The performance of each submission will be evaluated using F1-score based on the predicted labels and the gold ones. Participants will be provided with an evaluation script and a starter kit that includes a simple baseline.

## Important Dates


| Description                   | Deadline                                        |
|-------------------------------|------------------------------------------------|
| Sample Data Ready             | 15 July 2024                                  |
| Training Data Ready           | 02 September 2024                         |
| Evaluation Start              | 10 January 2025                                 |
| Evaluation End                | 31 January 2025                                 |
| System Description Paper Due  | 28 February 2025                               |
| Notification to authors       | 31 March 2025                                   |
| Camera ready due              | 21 April 2025                                   |
| SemEval workshop 2025         | (co-located with a major NLP conference)   |

## How to Participate

1. **Register**: Sign up on the Codalab competition platform (link to be provided).
2. **Download**: Access the datasets and starter kit from the repository (to be provided).
3. **Develop**: Build your models using the provided data and baseline.
4. **Submit**: Upload your predictions on the Codalab competition  platform (link to be provided)


## Competition Rules and Terms

<details>
  <summary>1. Consent to Public Release of Scores</summary>
  <p>By submitting results, you consent to the public release of your scores on the competition website, at the designated workshop, and in associated proceedings.</p>
  <p>Task organizers have discretion over the release and choice of metrics.</p>
  <p>Scores may include automatic and manual quantitative judgments, qualitative judgments, and other metrics as deemed appropriate.</p>
</details>

<details>
  <summary>2. Score Release and Validity</summary>
  <p>Task organizers reserve the right to withhold scores for incomplete, erroneous, deceptive, or rule-violating submissions.</p>
  <p>Inclusion of a submission's scores does not constitute endorsement.</p>
</details>

<details>
  <summary>3. Team Participation Rules</summary>
  <p>Participants may be involved in only one team.</p>
  <p>Exceptions may be granted with prior approval from organizers.</p>
</details>

<details>
  <summary>4. Account Management</summary>
  <p>Each team must create and use exactly one account on the designated platform.</p>
</details>

<details>
  <summary>5. Team Constitution</summary>
  <p>Team membership cannot be changed after the evaluation period begins.</p>
</details>

<details>
  <summary>6. Development Period Rules</summary>
  <p>Teams can submit up to 999 submissions.</p>
  <p>Results are visible only to the submitting team.</p>
  <p>Leaderboard is disabled.</p>
  <p>Warnings and errors are visible for each submission.</p>
</details>

<details>
  <summary>7. Evaluation Period Rules</summary>
  <p>Teams are limited to 3 submissions.</p>
  <p>Only the final submission is considered official.</p>
  <p>Warnings and errors are visible for each submission.</p>
</details>

<details>
  <summary>8. Post-Competition</summary>
  <p>Gold labels will be released after the competition.</p>
  <p>Teams are encouraged to report results on all system variants in their description paper.</p>
  <p>Official submission results must be clearly indicated.</p>
</details>

<details>
  <summary>9. Public Release of Submissions</summary>
  <p>Final team submissions may be made public after the evaluation period.</p>
</details>

<details>
  <summary>10. Disclaimer on Datasets</summary>
  <p>Organizers and affiliated institutions provide no warranties on dataset correctness or completeness.</p>
  <p>They are not liable for dataset access or usage.</p>
</details>

<details>
  <summary>11. Peer Review Process</summary>
  <p>Each participant will review another team's system description paper.</p>
</details>

<details>
  <summary>12. Dataset Usage Restrictions</summary>
  <p>Datasets should only be used for scientific or research purposes.</p>
  <p>Any other use is explicitly prohibited.</p>
  <p>Datasets must not be redistributed or shared with third parties.</p>
  <p>Interested parties should be directed to the official website.</p>
</details>


## Organizers


##  Resources

1. [SemEval 2024 Shared Tasks](https://semeval.github.io/SemEval2024/tasks)
2. [Frequently Asked Questions about SemEval](https://semeval.github.io/faq.html)
3. [Paper Submission Requirements](https://semeval.github.io/paper-requirements.html)
4. [Guidelines for Writing Papers](https://semeval.github.io/system-paper-template.html)
5. [Paper style files](https://github.com/acl-org/acl-style-files)
6. Paper submission link (TBD)

