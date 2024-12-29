
<!-- 
<p align="center" style="max-width: 80%; margin: 0 auto;">
  <img src="assets/bridging_emotion.png" style="width: 100%; height: auto;" />
    <h1 align="center"> </h1>
</p>

 -->

<p align="center" style="overflow: hidden; height: 300px; width: 400px; position: relative;">
  <img align="center" src="assets/bridge-logo.png" style="position: absolute; bottom: -50px; width: 100%;" />
</p>



<!-- 
# SemEval-2025 Task 11: Bridging the Gap in Text-Based Emotion Detection
 -->

---
# Join us

[Google Group](https://groups.google.com/g/emotion-semeval-2025-participants) | [Create an Issue](https://github.com/emotion-analysis-project/SemEval2025-task11/issues) | [Join Discord](https://discord.gg/g2xJtSbWhs) | [Contact Us](mailto:emotion-semeval-2025-organisers@googlegroups.com) | [Visit competition website](https://www.codabench.org/competitions/3863/) | [Download Dataset](https://docs.google.com/document/d/1yETTEiD8JVL8oeXu8Dvwc7OgPIDp0ROxd9nXifsXYYE/edit?usp=sharing) | [How to Participate](https://docs.google.com/document/d/1yETTEiD8JVL8oeXu8Dvwc7OgPIDp0ROxd9nXifsXYYE/edit)|

---
# Content

- [Join us](#join-us)
- [Content](#content)
- [📢 **News**](#-news)
    - [**16 September 2024**](#16-september-2024)
    - [**10 September 2024**](#10-september-2024)
- [Bridging the Gap in Text-Based Emotion Detection](#bridging-the-gap-in-text-based-emotion-detection)
- [Languages](#languages)
- [Tracks](#tracks)
    - [Track A: Multi-label Emotion Detection](#track-a-multi-label-emotion-detection)
    - [Track B: Emotion Intensity](#track-b-emotion-intensity)
    - [Track C: Cross-lingual Emotion Detection](#track-c-cross-lingual-emotion-detection)
- [Dataset and Download Links](#dataset-and-download-links)
- [Evaluation](#evaluation)
- [Important Dates and Task Phases](#important-dates-and-task-phases)
- [How to Participate](#how-to-participate)
- [Competition Rules and Terms](#competition-rules-and-terms)
- [Dataset paper](#dataset-paper)
- [Communication](#communication)
- [FAQs](#faqs)
- [Resources](#resources)
- [References](#references)
- [Organizers](#organizers)


# 📢 **News**



### **16 September 2024**


- The competition website is now updated on Codabench: [Codabench Competition](https://www.codabench.org/competitions/3863/).
- The dataset is now available on the competition website. If you previously downloaded the dataset via Google Drive, please download the updated version from the competition website as the data has been revised.
- To download the data, follow the instructions provided [here](https://docs.google.com/document/d/1yETTEiD8JVL8oeXu8Dvwc7OgPIDp0ROxd9nXifsXYYE/edit?usp=sharing).
  
### **10 September 2024**

- We have released the training and development datasets for **seven languages**: English (eng), German (deu), Oromo (orm), Brazilian Portuguese (ptbr),  Russian (rus), and Somali (som), and Tigrinya (tig). More languages are on the way, and we’ll be updating the table below table with release information over the next few days.
- The competition website will be live soon. Stay tuned for more updates!


# Bridging the Gap in Text-Based Emotion Detection

Emotions are simultaneously familiar and mysterious. On the one hand, we all express and manage our emotions every day. Yet, on the other hand, emotions are complex, nuanced, and sometimes hard to articulate. 

We use language in subtle and complex ways to express emotion (Wiebe et al. 2005, Mohammad and Kiritcheko 2018, Mohammad et al. 2018). Further, people are highly variable in how they perceive and express emotions (even within the same culture or social group). Thus, we can never truly identify how one is feeling based on something that they have said with absolute certainty. 

Emotion recognition is not one task but an umbrella term for several tasks such as detecting the emotions of the speaker, identifying what emotion a piece of text is conveying and detecting emotions evoked in a reader (Mohammad 2021, Mohammad 2023). 


This task is on **perceived emotions** and focuses on:

- **Determining what emotion most people will think the speaker may be feeling given a sentence or a short text snippet uttered by the speaker.**

The task is **not** about:

- The emotion evoked in the reader.
- The emotion of someone else mentioned in the text.
- Or **even** the true emotion of the speaker (which cannot be definitively known from just a short text snippet).

We acknowledge the importance of this distinction as perceived emotions can differ from actual emotions due to various factors such as cultural context, individual differences in emotional expression, and the limitations of text-based communication (Van Woensel and Nevil 2019, Wakerfield 2021).


# Languages

We include a large number of languages with many predominantly spoken in regions characterised by a relatively limited availability of NLP resources (e.g., Africa, Asia, Eastern Europe and Latin America):


[Afrikaans](https://en.wikipedia.org/wiki/Afrikaans), [Algerian Arabic](https://en.wikipedia.org/wiki/Algerian_Arabic), [Amharic](https://en.wikipedia.org/wiki/Amharic), [Brazilian Portuguese](https://en.wikipedia.org/wiki/Brazilian_Portuguese), [Chinese](https://en.wikipedia.org/wiki/Chinese_language), [English](https://en.wikipedia.org/wiki/English_language), [German](https://en.wikipedia.org/wiki/German_language), [Hausa](https://en.wikipedia.org/wiki/Hausa_language), [Hindi](https://en.wikipedia.org/wiki/Hindi), [Igbo](https://en.wikipedia.org/wiki/Igbo_language),  [Javanese](https://en.wikipedia.org/wiki/Javanese_language), [Indonesian](https://en.wikipedia.org/wiki/Indonesian_language), [isiXhosa](https://en.wikipedia.org/wiki/Xhosa_language), [isiZulu](https://en.wikipedia.org/wiki/Zulu_language), [Kinyarwanda](https://en.wikipedia.org/wiki/Kinyarwanda),  [Marathi](https://en.wikipedia.org/wiki/Marathi_language), [Latin American Spanish](https://en.wikipedia.org/wiki/Spanish_language_in_the_Americas), [Moroccan Arabic](https://en.wikipedia.org/wiki/Moroccan_Arabic), [Mozambican Portuguese](https://en.wikipedia.org/wiki/Mozambican_Portuguese), [Nigerian-Pidgin](https://en.wikipedia.org/wiki/Nigerian_Pidgin), [Oromo](https://en.wikipedia.org/wiki/Oromo_language), [Romanian](https://en.wikipedia.org/wiki/Romanian_language), [Russian](https://en.wikipedia.org/wiki/Russian_language), [Setswana](https://en.wikipedia.org/wiki/Tswana_language), [Somali](https://en.wikipedia.org/wiki/Somali_language), [Swahili](https://en.wikipedia.org/wiki/Swahili_language), [Sundanese](https://en.wikipedia.org/wiki/Sundanese_language), [Swedish](https://en.wikipedia.org/wiki/Swedish_language), [Tatar](https://en.wikipedia.org/wiki/Tatar_language), [Tigrinya](https://en.wikipedia.org/wiki/Tigrinya_language), [Twi](https://en.wikipedia.org/wiki/Twi),[Xitsonga](https://en.wikipedia.org/wiki/Tsonga_language), [Ukrainian](https://en.wikipedia.org/wiki/Ukrainian_language), [Yoruba](https://en.wikipedia.org/wiki/Yoruba_language).




# Tracks

Participants can participate in one or more of the following tracks:


### Track A: Multi-label Emotion Detection 
Given a target text snippet, predict the **perceived emotion(s) of the speaker**. Specifically, select whether each of the following emotions apply: **joy**, **sadness**, **fear**, **anger**, **surprise**, or **disgust**. In other words, label the text snippet with:
joy (**1**) or no joy (**0**), sadness (**1**) or no sadness (**0**), anger (**1**) or no anger (**0**), surprise (**1**) or no surprise (**0**), and disgust (**1**) or no disgust (**0**).

**Note that for some languages such as English, the set perceived emotions includes 5 emotions: joy, sadness, fear, anger, or surprise and does not include disgust.** 


A training dataset with gold emotion labels will be provided for this track. 

Below is a sample of the English training data (Track A). A text snippet can have multiple emotions (e.g., the sentence with the ID **sample_05** expresses both joy and surprise), or none (e.g., **sample_04** with all the emotion values equal to 0 is considered neutral).

<img src="https://github.com/user-attachments/assets/73ca700f-6dcc-4dec-8001-75a7842e0cae" alt="Sample Training DataA" width="100%">


### Track B: Emotion Intensity
Given a target text  and a target perceived emotion, predict the intensity for each of the classes. 

The set of the perceived emotions includes: **joy**, **sadness**, **fear**, **anger**, **surprise**, or **disgust**.

The set of ordinal intensity classes includes:
**0** for no emotion, **1** for a low degree of emotion, **2** for a moderate degree of emotion, and **3** for a high degree of emotion.

Below is a sample of the English training data (Track B). For each emotion, the value associated with it indicates its degree of intensity. For example, **sample_05** has a value of 3 for joy and a value of 3 for surprise, i.e., **high degrees** of joy and surprise in the text snippet.

<img src="https://github.com/user-attachments/assets/daeefcd8-f4b6-46c3-a692-8d8477d1dc11" alt="Sample Training DataB" width="100%">


**Note that for some languages such as English, the set perceived emotions includes 5 emotions: joy, sadness, fear, anger, or surprise and does not include disgust.** 

### Track C: Cross-lingual Emotion Detection 
Given a labeled training set in one of the languages given [above](#languages), predict the perceived emotion labels of a new text instance in a different target language. 

The set of the six perceived emotion classes includes: **joy**, **sadness**, **fear**, **anger**, **surprise**, or **disgust**.

**Note that for some languages such as English, the set perceived emotions includes 5 emotions: joy, sadness, fear, anger, or surprise and does not include disgust.** 

# Dataset and Download Links

 - Visit the official competition page on Codabench: https://www.codabench.org/competitions/3863/
 - Follow the detailed instructions provided [here](https://docs.google.com/document/d/1yETTEiD8JVL8oeXu8Dvwc7OgPIDp0ROxd9nXifsXYYE/edit?usp=sharing) to download the data.

<!-- 
For each track, we provide the sample, training, and evaluation datasets. Find the links to download the datasets for each track below:

| Track | Download Link | File ID |
|-------|------------|---------|
| Track A | [Track A Dataset](https://drive.google.com/drive/folders/1Pvptx6XDsfLcR0IGvGUV4ZDD1qezyzUo?usp=share_link) | `1Pvptx6XDsfLcR0IGvGUV4ZDD1qezyzUo` |
| Track B  | [Track B Dataset](https://drive.google.com/drive/folders/1OCzDN5RuWdos47P3TvIzIqVcspf1_4yZ?usp=share_link) | `1OCzDN5RuWdos47P3TvIzIqVcspf1_4yZ` |
| Track C | [Track C Dataset](#) | `` |
| All Tracks | [Complete Dataset](https://drive.google.com/drive/folders/1vYggpyd0O0FNL99OvHHUp_wsCKVOcZWn?usp=share_link) | `1vYggpyd0O0FNL99OvHHUp_wsCKVOcZWn` |


Download the dataset using [gdown](https://github.com/wkentaro/gdown):

1. Install gdown if you haven't already:

   ```pip install gdown```

2. Use the following commands to download the datasets using the provided IDs:

   ```gdown --folder https://drive.google.com/drive/folders/<file_id> ```
   
-->

<!-- 
The table below presents the class distribution for the currently released languages. Please note that while some languages include the 'Disgust' class, others do not. We will be adding more languages in future releases, so please check back for updates.
# Class Distribution Per Language

## Training Data


| S/N | Language             | Language Code | Joy  | Surprise | Sadness | Disgust | Fear | Anger | Neutral | Total |
|-----|----------------------|---------------|------|----------|---------|---------|------|-------|---------|-------|
| 1   | English              | eng           | 674  | 839      | 878     | --      | 1611 | 333   | 239     | 4574  |
| 2   | German               | deu           | 541  | 159      | 516     | 832     | 239  | 768   | 645     | 3700  |
| 3   | Brazilian Portuguese | ptbr          | 581  | 153      | 322     | 75      | 109  | 718   | 632     | 2590  |



## Development Data

| S/N | Language             | Language Code | Joy | Surprise | Sadness | Disgust | Fear | Anger | Neutral | Total |
|-----|----------------------|---------------|-----|----------|---------|---------|------|-------|---------|-------|
| 1   | English              | eng           | 31  | 31       | 35      | --      | 63   | 16    | 13      | 189   |
| 2   | German               | deu           | 40  | 15       | 48      | 61      | 20   | 61    | 49      | 294   |
| 3   | Brazilian Portuguese | ptbr          | 62  | 21       | 28      | 5       | 8    | 58    | 46      | 228   |

 -->

The table below shows the languages of the different datasets, their sizes and the release status of their pilot samples, training, and development (dev) sets. Note that ✓ means released and can be found in the data folder. Please note that some languages include the Disgust class, while others do not.




| No. | Language              | Code | Track 1 | Track 2 | Track 3 |
|-----|-----------------------|------|---------|---------|---------|
| 1   | [Afrikaans](https://en.wikipedia.org/wiki/Afrikaans)             | AFR  | ✓       |     X     | ✓       |
| 2   | [Algerian Arabic](https://en.wikipedia.org/wiki/Algerian_Arabic)       | ARQ  | ✓       |         | ✓       |  
| 3   | [Amharic](https://en.wikipedia.org/wiki/Amharic)               | AMH  | ✓       | ✓       | ✓       |
| 4   | [Brazilian Portuguese](https://en.wikipedia.org/wiki/Brazilian_Portuguese)  | PTBR | ✓       | ✓       | ✓       |
| 5   | [Chinese](https://en.wikipedia.org/wiki/Chinese_language)               | ZHO  | ✓       |    ✓      | ✓       |
| 6   | [Emakhuwa](https://en.wikipedia.org/wiki/Makhuwa_language)                | VMW  | ✓       |         | ✓       |
| 7   | [English](https://en.wikipedia.org/wiki/English_language)               | ENG  | ✓       | ✓       | ✓       |
| 8   | [German](https://en.wikipedia.org/wiki/German_language)                | DEU  | ✓       | ✓       | ✓       |
| 9   | [Hausa](https://en.wikipedia.org/wiki/Hausa_language)                 | HAU  | ✓       |      ✓      | ✓       | 
| 10  | [Hindi](https://en.wikipedia.org/wiki/Hindi)                 | HIN  | ✓       |         | ✓       | 
| 11  | [Igbo](https://en.wikipedia.org/wiki/Igbo_language)                  | IBO  | ✓       |         | ✓       |
| 12  | [Indonesian](https://en.wikipedia.org/wiki/Indonesian_language)            | IND  | X       |         | ✓       |  
| 13  | [isiXhosa](https://en.wikipedia.org/wiki/Xhosa_language)              | XHO  | ✓       |         | ✓       |
| 14  | [isiZulu](https://en.wikipedia.org/wiki/Zulu_language)               | ZUL  | ✓       |         | ✓       |
| 15  | [Javanese](https://en.wikipedia.org/wiki/Javanese_language)              | JAV  | ✓       |         | ✓       |
| 16  | [Kinyarwanda](https://en.wikipedia.org/wiki/Kinyarwanda)           | KIN  | ✓       |         | ✓       |
| 17  | [Spanish (Latin American)](https://en.wikipedia.org/wiki/Spanish_language_in_the_Americas) | ESP  | ✓       |   ✓        | ✓       |
| 18  | [Marathi](https://en.wikipedia.org/wiki/Marathi_language)               | MAR  | ✓       |         | ✓       | 
| 19  | [Moroccan Arabic](https://en.wikipedia.org/wiki/Moroccan_Arabic)       | ARY  | ✓       |         | ✓       |  
| 20  | [Mozambican Portuguese](https://en.wikipedia.org/wiki/Mozambican_Portuguese) | PTM  | ✓       |         | ✓       |  
| 21  | [Nigerian-Pidgin](https://en.wikipedia.org/wiki/Nigerian_Pidgin)       | PCM  | ✓       |         | ✓       | 
| 22  | [Oromo](https://en.wikipedia.org/wiki/Oromo_language)                 | ORM  | ✓       | ✓       | ✓       | 
| 23  | [Romanian](https://en.wikipedia.org/wiki/Romanian_language)              | RON  | ✓       |    ✓       | ✓       | 
| 24  | [Russian](https://en.wikipedia.org/wiki/Russian_language)               | RUS  | ✓       | ✓       | ✓       | 
| 25  | [Somali](https://en.wikipedia.org/wiki/Somali_language)                | SOM  | ✓       | ✓       | ✓       | 
| 26  | [Sundanese](https://en.wikipedia.org/wiki/Sundanese_language)             | SUN  | X       |         | ✓       | 
| 27  | [Swahili](https://en.wikipedia.org/wiki/Swahili_language)               | SWA  | ✓       |         | ✓       |  
| 28  | [Swedish](https://en.wikipedia.org/wiki/Swedish_language)               | SWE  | ✓       |         | ✓       |
| 29  | [Tatar](https://en.wikipedia.org/wiki/Tatar_language)                 | TAT  | ✓       |         | ✓       |
| 30  | [Tigrinya](https://en.wikipedia.org/wiki/Tigrinya_language)              | TIR  | ✓       | ✓       | ✓       |
| 31  | [Ukrainian](https://en.wikipedia.org/wiki/Ukrainian_language)             | UKR  | ✓       |         | ✓       |
| 32  | [Yoruba](https://en.wikipedia.org/wiki/Yoruba_language)                | YOR  | ✓       |         | ✓       |









# Evaluation

The performance of the submitted systems will be evaluated based on the following metrics:


- <b> Track A: Multilabel Emotion Detection</b> 
  The evaluation metric will be the F-score based on the predicted labels and the gold ones.

- <b> Track B: Emotion Intensity</b> 
    The evaluation metric will be the Pearson correlation between the predicted labels and the gold ones.

- <b>Track C: Crosslingual Emotion Detection</b> 
  The evaluation metric will be the F-score based on the predicted labels and the gold ones.

Participants will be provided with an evaluation script and a starter kit that includes a simple baseline.

- For details about the evaluation script and the format checker, check this [guide](https://github.com/emotion-analysis-project/SemEval2025-Task11-Evaluation).

# Important Dates and Task Phases


| Description                   | Deadline                                        |
|-------------------------------|------------------------------------------------|
| Sample Data Ready             | ~~15 July 2024~~                                  |
| Training Data Ready           | 10 September 2024                         |
| Evaluation Start              | 10 January 2025                                 |
| Evaluation End                | 31 January 2025                                 |
| System Description Paper Due  | 28 February 2025                               |
| Notification to authors       | 31 March 2025                                   |
| Camera ready due              | 21 April 2025                                   |
| SemEval workshop 2025         | (co-located with a major NLP conference)   |


The task will be divided into three phases: Development, Evaluation, and Post-Evaluation. The following summarize the phases and their timelines.


<details>
    <summary><strong>Development Phase:</strong> Codalab submission link coming soon</summary>
    <ul>
      <li>This phase runs from 02 September to 10 January 2024.</li>
      <li>Train (with gold labels) and dev data (without gold labels) will be released for this phase.</li>
      <li>Train and evaluate your model on the dev set via CodaLab.</li>
      <li>Up to 999 submissions are allowed, and the leaderboard is open for you to view your results and those of others.</li>
    </ul>
  </details>

  <details>
    <summary><strong>Evaluation Phase:</strong> Codalab submission link coming soon</summary>
    <ul>
      <li>This phase runs from around 10 January to 31 January 2024 (tentative).</li>
      <li>Test data will be released (without gold labels).</li>
      <li>Participants will have the opportunity to evaluate their models on the test data.</li>
      <li>Each team is allowed only one submission. This single submission will be considered your official entry for the competition.</li>
      <li>The leaderboard is disabled and will only be published after the submission deadline.</li>
    </ul>
  </details>

  <details>
    <summary><strong>Post-Evaluation Phase:</strong>  Codalab submission link coming soon</summary>
    <ul>
      <li>Starts around 31 January 2024 and never ends.</li>
      <li>In this phase, you can still submit and test your system even after the official competition ends. This way, you can keep improving your work.</li>
      <li>We will make the leaderboard public again so you can see how you are doing compared to others.</li>
      <li>You can use CodaLab to talk with other participants, share ideas, and learn how to make your system better.</li>
    </ul>
  </details>



# How to Participate

1. **Register**: Sign up on the CodaBench competition platform.
2. **Track**: Decide on the track(s) you want to participate in (Track A, B and/or C).
3. **Download**: Access to the datasets for each track will be provided in this repository.
4. **Develop**: Build your models using the provided data.
5. **Submit**: Submit your predictions on the CodaBench competition platform.

Follow the guides [here](https://docs.google.com/document/d/1yETTEiD8JVL8oeXu8Dvwc7OgPIDp0ROxd9nXifsXYYE/edit?usp=sharing) 




# Competition Rules and Terms
<details>
  <summary>1. Consent to Public Release of Scores</summary>
  <ul>
    <li>By submitting results, you consent to the public release of your scores on:
      <ul>
        <li>the competition website,</li>
        <li>at the designated workshop,</li>
        <li>in associated proceedings.</li>
      </ul>
    </li>
    <li>Task organizers have discretion over the release and choice of metrics.</li>
    <li>Scores may include:
      <ul>
        <li>automatic and manual quantitative judgments,</li>
        <li>qualitative judgments,</li>
        <li>other metrics as deemed appropriate.</li>
      </ul>
    </li>
  </ul>
</details>

<details>
  <summary>2. Score Release and Validity</summary>
  <ul>
    <li>Task organizers reserve the right to withhold scores for:
      <ul>
        <li>incomplete submissions,</li>
        <li>erroneous submissions,</li>
        <li>deceptive submissions,</li>
        <li>rule-violating submissions.</li>
      </ul>
    </li>
    <li>Inclusion of a submission's scores does not constitute endorsement.</li>
  </ul>
</details>

<details>
  <summary>3. Team Participation Rules</summary>
  <ul>
    <li>Participants may be involved in only one team.</li>
    <li>Exceptions may be granted with prior approval from organizers.</li>
  </ul>
</details>

<details>
  <summary>4. Account Management</summary>
  <ul>
    <li>Each team must create and use exactly one account on the designated platform.</li>
  </ul>
</details>

<details>
  <summary>5. Team Constitution</summary>
  <ul>
    <li>Team membership cannot be changed after the evaluation period begins.</li>
  </ul>
</details>

<details>
  <summary>6. Development Period Rules</summary>
  <ul>
    <li>Teams can submit up to 999 submissions.</li>
    <li>Results are visible only to the submitting team.</li>
    <li>Leaderboard is disabled.</li>
    <li>Warnings and errors are visible for each submission.</li>
  </ul>
</details>

<details>
  <summary>7. Evaluation Period Rules</summary>
  <ul>
    <li>The teams are contrained to make 3 submissions.</li>
    <li>Only the final submission will be considered official.</li>
    <li>Warnings and errors are visible for each submission.</li>
  </ul>
</details>

<details>
  <summary>8. Post-Competition</summary>
  <ul>
    <li>The gold labels will be released after the competition.</li>
    <li>The teams are encouraged to report results on all their system variants in their description paper.</li>
    <li>The official submission results must be clearly indicated.</li>
  </ul>
</details>

<details>
  <summary>9. Public Release of Submissions</summary>
  <ul>
    <li>Final team submissions may be made public after the evaluation period.</li>
  </ul>
</details>

<details>
  <summary>10. Disclaimer about the Datasets</summary>
  <ul>
    <li>Organizers and affiliated institutions provide no warranties on dataset correctness or completeness.</li>
    <li>They are not liable for dataset access or usage.</li>
  </ul>
</details>

<details>
  <summary>11. Peer Review Process</summary>
  <ul>
    <li>Each participant will review another team's system description paper.</li>
  </ul>
</details>

<details>
  <summary>12. Dataset Usage Restrictions</summary>
  <ul>
    <li>Datasets should only be used for scientific or research purposes.</li>
    <li>Any other use is explicitly prohibited.</li>
    <li>Datasets must not be redistributed or shared with third parties.</li>
    <li>Interested parties should be directed to the official website.</li>
  </ul>
</details>
<details>
  <summary>13. Final ranking</summary>
  <ul>
    <li>To be included in the official task ranking, you **MUST** submit a system description paper.</li>
  </ul>
</details>

# Dataset paper

We will soon release a dataset paper that describes the data collection, annotation process, and baseline experiments. This paper will provide additional details and information that will be useful for the task participants.


# Communication

- Join our [Discord Channel](https://discord.gg/g2xJtSbWhs) to ask questions and receive updates (coming soon).
- If you have any questions or issues, please feel free to [create an issue](https://github.com/emotion-analysis-project/SemEval2025-task11/issues).
- Contact organizers at: emotion-semeval-2025-organisers[at]googlegroups[dot]com



# FAQs
<details>
  <summary>Do I have to participate in all languages for a given track?</summary>
  <ul>
    <li>No, you can participate in one or more languages.</li>
  </ul>
</details>

<details>
  <summary>How will you verify my submitted model?</summary>
  <ul>
    <li>To be included in the final team rankings of our shared task, it is mandatory for participants to submit a system description paper describing their approaches and methodologies in detail, therefore ensuring scientific integrity.</li>
  </ul>
</details>

<details>
  <summary>When will you release the gold labels?</summary>
  <ul>
    <li>For the dev set, the gold labels will be released when the evaluation phase starts and the gold labels for the different test sets will be released after the competition is over.</li>
  </ul>
</details>

<details>
  <summary>Can I use LLMs in the different tracks?</summary>
  <ul>
    <li>Yes.</li>
  </ul>
</details>
<details>
<summary>Can I use additional datasets (e.g, publicly provided ones from other sources)?</summary>
  <ul>
    <li>Yes. Please do cite them in the system description paper.</li>
  </ul>
</details>
<details>
  <summary>How was the data collected?</summary>
   <ul>
    <li>
   The data collection process a standard one, you can check previous papers in the area to have an idea (e.g., https://aclanthology.org/S18-1001.pdf). We have data instances (text snippets) annotated by >3 annotators. The annotators       decide whether some emotion is present in a given instance (text snippet). 
   For details about the data sources, annotation guidelines, number of annotators per language, etc., this information will be shared in the dataset paper.
    </li>
   </ul>
</details>
<details>
  <summary>How was the data annotated and did you use LLMs to annotate it?</summary>
   <ul>
    <li>
  No. The data instances were annotated by (>=3) native speakers and no LLMs were involved in the process. The annotators labeled the whole sentences not the words and they were expected to have different opinions as (1)this a subjective task and emotions are complex and (2)we were interested in the emotion(s) that they perceived. See the task definition for more details.
    </li>
   </ul>
</details>
<details>
  <summary>Will I be included in the final ranking if I do not write a system description paper?</summary>
  <ul>
    <li>No. You MUST write a system description paper to be included in the final ranking.</li>
  </ul>
</details>

<details>
  <summary>I have never written a system description paper. How can I write one?</summary>
  <ul>
    <li>We will have an online writing tutorial and share resources to help you write a system description paper.</li>
  </ul>
</details>

<details>
  <summary>Do I need to pay conference registration fees and/or attend SemEval for my paper to be published?</summary>
  <ul>
    <li>It is not required to attend the SemEval workshop for the paper to be published. You do not have to pay any registration fees if you do not attend the workshop. However, if you want to attend the workshop, you need to pay for attendance.</li>
  </ul>
</details>

<details>
  <summary> Our system did not perform very well, should I still write a system description paper? </summary>
 <ul>
    <li> We want to hear from **all** of you even if you did not outperform other systems!Write about the details of your system. (**Yes we want your insights from any negative results!**)</li>
  </ul>

</details>

#  Resources

2. [SemEval 2025 Shared Tasks](https://semeval.github.io/SemEval2025/tasks)
3. [Frequently Asked Questions about SemEval](https://semeval.github.io/faq.html)
4. [Paper Submission Requirements](https://semeval.github.io/paper-requirements.html)
5. [Guidelines for Writing Papers](https://semeval.github.io/system-paper-template.html)
6. [Paper style files](https://github.com/acl-org/acl-style-files)
7. Previous shared-tasks on emotion detection [SemEval-2018 Task 1: Affect in Tweets](https://aclanthology.org/S18-1001)
8. **Resources for Beginners**
   - [Starter kit](baseline.ipynb) (Note that you need to donload the data from CodaBench.)
   - Writing tutorial: [Blogpost](https://github.com/nedjmaou/Writing_a_task_description_paper)
   - Examples of additional datasets/lexicons:
      - Emotion lexicons: http://saifmohammad.com/WebPages/lexicons.html 
      - [SemEval-2018 Task 1: Affect in Tweets](https://aclanthology.org/S18-1001) for arb, eng, esp.
      - [Emotions in Drama](https://github.com/lauchblatt/Emotions_in_Drama) for deu.
      - [RESD](https://paperswithcode.com/dataset/resd), [CEDR-M7](https://huggingface.co/datasets/Aniemore/cedr-m7), [Dusha](https://github.com/salute-developers/golos/tree/master/dusha#dusha-dataset) for rus.
10. Paper submission link (to be added)


# References 
Janyce Wiebe, Theresa Wilson, and Claire Cardie. "Annotating expressions of opinions and emotions in language." Language resources and evaluation 39 (2005): 165-210.

Saif M. Mohammad,, and Svetlana Kiritchenko. "Understanding Emotions: A Dataset of Tweets to Study Interactions between Affect Categories." Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018).

Saif M. Mohammad, Felipe Bravo-Marquez, Mohammad Salameh, and Svetlana Kiritchenko: SemEval-2018 Task 1: Affect in Tweets. In Proceedings of the International Workshop on Semantic Evaluation (SemEval-2018).

Lieve Van Woensel and Nissy Nevil. 2019. What if your emotions were tracked to spy on you? European Parliamentary Research Service, PE 634.415. https://www.europarl.europa.eu/RegData/etudes/ATAG/2019/634415/EPRS_ATA(2019)634415_EN.pdf.

Jane Wakefield. 2021. AI emotion-detection software tested on Uyghurs. BBC. https://www.bbc.com/news/technology-57101248.

Saif M.  Mohammad "Ethics sheet for automatic emotion recognition and sentiment analysis." Computational Linguistics 48.2 (2022): 239-278.

Saif M. Mohammad "Best Practices in the Creation and Use of Emotion Lexicons." Findings of the Association for Computational Linguistics (EACL 2023).


# Organizers

[Shamsuddeen Hassan Muhammad](https://shmuhammadd.github.io/), [Seid Muhie Yimam ](https://seyyaw.github.io/) , [Nedjma Ousidhoum](https://nedjmaou.github.io/),
[Idris Abdulmumin](https://abumafrim.github.io/), [David Ifeoluwa Adelani](https://dadelani.github.io/), [Ibrahim Said Ahmad](https://isahmadbbr.github.io/), [Alham Fikri Aji](https://afaji.github.io/), [Felermino Ali](https://felerminoali.github.io/#about), [Vladimir Araujo](https://vgaraujov.github.io/),
[Abinew Ali Ayele](https://www.inf.uni-hamburg.de/en/inst/ab/lt/people/abinew-ali.html),[Meriem Beloucif](https://belomeriem.github.io), [Christine de Kock](https://christinedekock.com), [Oana Ignat](https://oanaignat.github.io), [Alexander Panchenko](https://faculty.skoltech.ru/people/alexanderpanchenko), [Terry Ruas](https://terryruas.com/), Nirmal Surange, [Daniela Teodorescu](https://dteodore.github.io/),
[Jan Philip Wahle](https://jpwahle.com/), [Yi Zhou](https://jodiechou.github.io), [Saif M. Mohammad](https://www.saifmohammad.com/)



<!-- 

# Ethical statement

# License

Shield: [![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

<!-- 
<p align="center" style="max-width: 80%; margin: 0 auto;">
  <img src="assets/bridging_emotion.png" style="width: 100%; height: auto;" />
    <h1 align="center"> </h1>
</p>

 -->
