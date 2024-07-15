# SemEval-2025 Task 11 Datasets

These datasets are used for **SemEval-2025 Task 11: Bridging the Gap in Text-Based Emotion Detection** 😔😱😡.

For more information, visit the [official GitHub repository](https://github.com/emotion-analysis-project/SemEval2025-task11).

## Dataset Information

Our collection includes datasets in multiple languages designed for research on text-based emotion detection and related tasks. They contain text instances along with their annotations for various emotions. 

### Track 1 (Emotion Classification)

For track 1, each entry in a given dataset consists of a unique identifier, a text sample, and seven columns representing different emotions: Joy, Fear, Anger, Sadness, Disgust, Neutral, and Surprise. Each emotion column is binary, where 0 indicates the absence of the emotion and 1 indicates its presence. Note that a single text can express multiple emotions simultaneously. The columns are named as follows:

- **id**: the unique identifier of a given instance.
- **text**: the annotated textual instance.
- **Joy**: binary labeled. 0 indicates the absence of joy in the text, and 1 indicates its presence.
- **Fear**: binary labeled. 0 indicates the absence of fear in the text, and 1 indicates its presence.
- **Anger**: binary labeled. 0 indicates the absence of anger in the text, and 1 indicates its presence.
- **Sadness**: binary labeled. 0 indicates the absence of sadness in the text, and 1 indicates its presence.
- **Disgust**: binary labeled. 0 indicates the absence of disgust in the text, and 1 indicates its presence.
- **Neutral**: binary labeled. 1 indicates that the text in neutral and  and 0 indicates that it is not.
- **Surprise**: binary labeled. 0 indicates the absence of surpise in the text, and 1 indicates its presence.

#### Sample Data Instance

| id                      | text                                                                                          | Joy | Fear | Anger | Sadness | Disgust | Neutral | Surprise |
|-------------------------|-----------------------------------------------------------------------------------------------|-----|------|-------|---------|---------|---------|----------|
| eng_sample_track1_00001 | The coronavirus was created to cause fear and panic among people                              | 0   | 1    | 1     | 0       | 0       | 0       | 0        |


### Track 2 (Ordinal Intensity)

For track 2, each entry in a given dataset includes a unique identifier, a text, the dominant emotion expressed in the text, and an intensity class representing the strength of the emotion on a scale from 0 to 3, with 0 indicating the absence of emotion and 3 indicating the highest level of intensity. Such as:


- **id**: the unique identifier of a given instance.
- **text**: the annotated textual instance.
- **emotion**: the primary emotion expressed in the text.
- **intensity_class**: the intensity level of the emotion (0:no emotion, 1: low emotion, 2: medium emotion, and 3: high intensity).

#### Sample Data Instance

| id                      | text                                                                                          | emotion | intensity_class |
|-------------------------|-----------------------------------------------------------------------------------------------|---------|-----------------|
| eng_sample_track2_00001 |APC has a bright future in the Southeast 	                                     | Joy     | 1               |


### Track 3

Same data format with Track 1. 


## Languages Included

We provide datasets in the following languages: 

| No. | Language              | Code | Sample Data Ready | Training Data  | Dev Data  | Size   |
|-----|-----------------------|------|-------------------|----------------------|----------------|--------|
| 1   | Afrikaans             | AFR  |                   |                      |                |        |
| 2   | Algerian Arabic       | ARQ  |                   |                      |                |        |
| 3   | Amharic               | AMH  |   ✓                |                      |                |        |
| 4   | Arabic                | ARB  |                   |                      |                |        |
| 5   | Brazilian Portuguese  | PTB  |                   |                      |                |        |
| 6   | Chinese               | ZHO  | ✓                |                      |                |        |
| 7   | English               | ENG  |                   |                      |                |        |
| 8   | German                | DEU  |                   |                      |                |        |
| 9   | Hausa                 | HAU  | ✓                 |                      |                |        |
| 10  | Hindi                 | HIN  |                   |                      |                |        |
| 11  | Igbo                  | IBO  |                   |                      |                |        |
| 12  | Indonesian            | IND  |                   |                      |                |        |
| 13  | isiXhosa              | XHO  |                   |                      |                |        |
| 14  | isiZulu               | ZUL  |                   |                      |                |        |
| 15  | Javanese              | JAV  |                   |                      |                |        |
| 16  | Kinyarwanda           | KIN  |                   |                      |                |        |
| 17  | Marathi               | MAR  |                   |                      |                |        |
| 18  | Moroccan Arabic       | ARY  |                   |                      |                |        |
| 19  | Mozambican Portuguese | PTM  |                   |                      |                |        |
| 20  | Nigerian-Pidgin       | PCM  |                   |                      |                |        |
| 21  | Oromo                 | ORM  |    ✓               |                      |                |        |
| 22  | Romanian              | RON  |                   |                      |                |        |
| 23  | Russian               | RUS  |    ✓               |                      |                |        |
| 24  | Setswana              | TSN  |                   |                      |                |        |
| 25  | Somali                | SOM  |      ✓             |                      |                |        |
| 26  | Spanish               | SPA  |                   |                      |                |        |
| 27  | Swahili               | SWA  |                   |                      |                |        |
| 28  | Swedish               | SWE  |                   |                      |                |        |
| 29  | Tatar                 | TAT  |      ✓             |                      |                |        |
| 30  | Tigrinya              | TIR  |     ✓              |                      |                |        |
| 31  | Ukrainian             | UKR  |                   |                      |                |        |
| 32  | Xitsonga              | TSO  |                   |                      |                |        |
| 33  | Yoruba                | YOR  |                   |                      |                |        |

## Citation

If you use our datasets, please cite our work as follows: **citation coming soon**


Contact organizers at: emotion-semeval-2025-organisers[at]googlegroups[dot]com

