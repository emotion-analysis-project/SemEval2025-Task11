# SemEval-2025 Task 11 Datasets

These datasets are used for **SemEval-2025 Task 11: Bridging the Gap in Text-Based Emotion Detection** 😔😱😡.

For more information, visit the [official GitHub repository](https://github.com/emotion-analysis-project/SemEval2025-task11).

## Dataset Information

Our dataset collection includes datasets in multiple languages. The datasets are designed for research on text-based emotion detection and related tasks, and contain text instances along with their annotations for various emotions. 

### Track 1 (Emotion Classification)

For the track 1 datasets, each entry in the dataset consists of a unique identifier, a text sample in Hausa, and seven columns representing different emotions: Joy, Fear, Anger, Sadness, Disgust, Neutral, and Surprise. Each emotion column is binary, where `0` indicates the absence of the emotion and `1` indicates its presence. Note: A single text sample can express multiple emotions simultaneously. 

Here are the components of the dataset:

- **id**: A unique identifier for each text.
- **text**: The actual text in the Hausa language.
- **Joy**: Indicates the presence (`1`) or absence (`0`) of joy in the text.
- **Fear**: Indicates the presence (`1`) or absence (`0`) of fear in the text.
- **Anger**: Indicates the presence (`1`) or absence (`0`) of anger in the text.
- **Sadness**: Indicates the presence (`1`) or absence (`0`) of sadness in the text.
- **Disgust**: Indicates the presence (`1`) or absence (`0`) of disgust in the text.
- **Neutral**: Indicates the presence (`1`) or absence (`0`) of a neutral tone in the text.
- **Surprise**: Indicates the presence (`1`) or absence (`0`) of surprise in the text.

### Sample Data

| id                      | text                                                                                          | Joy | Fear | Anger | Sadness | Disgust | Neutral | Surprise |
|-------------------------|-----------------------------------------------------------------------------------------------|-----|------|-------|---------|---------|---------|----------|
| eng_sample_track1_00001 | The coronavirus was created to cause fear and panic among people                              | 0   | 1    | 1     | 0       | 0       | 0       | 0        |


### Track 2 (Ordinal Intensity)

For the track 2 datasets, each entry includes a unique identifier, a text, the dominant emotion expressed in the text, and an intensity class indicating the strength of the emotion on a scale from 0 to 3, with 0 being no-emotion and 3 being the highest.

Here are the components of the dataset:

- **id**: A unique identifier for each text.
- **text**: The actual text in one of the language.
- **emotion**: The primary emotion expressed in the text.
- **intensity_class**: The intensity level of the emotion, ranging from 0 (no emotion) to 3 (high intensity).

### Sample Data

| id                      | text                                                                                          | emotion | intensity_class |
|-------------------------|-----------------------------------------------------------------------------------------------|---------|-----------------|
| eng_sample_track2_00001 |APC has a bright future in the Southeast 	                                     | Joy     | 1               |


### Languages Included

We provide datasets in the following languages: 

| No. | Language              | Code | Sample Data Ready | Training Data  | Dev Data  | Size   |
|-----|-----------------------|------|-------------------|----------------------|----------------|--------|
| 1   | Afrikaans             | AFR  |                   |                      |                |        |
| 2   | Algerian Arabic       | ARQ  |                   |                      |                |        |
| 3   | Amharic               | AMH  |                   |                      |                |        |
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
| 21  | Oromo                 | ORM  |                   |                      |                |        |
| 22  | Romanian              | RON  |                   |                      |                |        |
| 23  | Russian               | RUS  |                   |                      |                |        |
| 24  | Setswana              | TSN  |                   |                      |                |        |
| 25  | Somali                | SOM  |                   |                      |                |        |
| 26  | Spanish               | SPA  |                   |                      |                |        |
| 27  | Swahili               | SWA  |                   |                      |                |        |
| 28  | Swedish               | SWE  |                   |                      |                |        |
| 29  | Tatar                 | TAT  |                   |                      |                |        |
| 30  | Tigrinya              | TIR  |                   |                      |                |        |
| 31  | Ukrainian             | UKR  |                   |                      |                |        |
| 32  | Xitsonga              | TSO  |                   |                      |                |        |
| 33  | Yoruba                | YOR  |                   |                      |                |        |

## Citation

If you use our datasets, please cite our work as follows: **citation coming soon**

