 📊 **Dataset**



The dataset (`spotify\_data.csv`) contains 2017 rows and 17 columns.



**Relevant Features**:

\- *acousticness, danceability, duration\_ms, energy, instrumentalness*

*- loudness, tempo, valence, targe*t (a binary feature indicating if the song is liked or not)

\- *song\_title, artist*



 🛠️ **Installation \& Setup**



1\.  **Clone the repository**:

&nbsp;  ```bash

&nbsp;  git clone https://github.com/pranjalisdongre/Spotify-Data-Analysis

&nbsp;  cd Spotify-Data-Analysis

2\.  **Create a virtual environment:**

&nbsp;   python -m venv venv

&nbsp;   source venv/bin/activate    (On Mac/Linux)

&nbsp;   venv\\Scripts\\activate       (On Windows)



&nbsp;3. **Install dependencies:**

    **pip install -r requirements.txt**



**4.  Launch Jupyter Notebook:**



&nbsp;   jupyter notebook







🚀 **Usage**



1\.  Launch Jupyter Notebook:

    ```bash

    jupyter notebook

    ```

2\.  Navigate to the `notebooks/` folder and open `SPOTIFY (1).ipynb`.

3\.  Run the cells sequentially to see the entire analysis, from data loading to visualization.



🔍 **Analysis and Results**



 1. **Data Cleaning**

\- Loaded the dataset and inspected its structure.

\- Checked for and handled missing values (there were none).

\- Dropped the unnecessary `Unnamed: 0` index column.

\- Generated summary statistics using `.describe()`.



2\. **Top 5 Most Popular Artists**

Determined popularity by counting the number of tracks per artist.

!\[Top 5 Artists](images/top\_artists.png)

**Result**: The most prolific artists in the dataset are Drake, Rick Ross, Disclosure, Backstreet Boys, and WALK THE MOON.



 3. **Top 5 Loudest Tracks**

Sorted the dataset by the `loudness` feature (measured in decibels, dB). Lower values are quieter, higher values are louder.

!\[Top 5 Loudest Tracks](images/loudest\_tracks.png)

**Result**: The loudest tracks are primarily classical pieces, which often have a wide dynamic range captured in the recording.



 4. **Top 10 Instrumental Tracks**

Sorted the dataset by the `instrumentalness` feature (predicts whether a track contains no vocals).

!\[Top 10 Instrumental Tracks](images/instrumental\_tracks.png)

**Result**: The tracks with the highest instrumentalness scores are, unsurprisingly, electronic, metal, and jazz instrumentals.



 📈 **Key Takeaways**



\- **Data Quality**: The dataset was very clean from the start, requiring minimal preprocessing.

\- **Artist Output**: Understanding which artists have the most content on a platform can be valuable for music industry analysis.

\- **Audio Features**: Features like `loudness` and `instrumentalness` can be used to create very specific playlists.



🤝 **Contributing**



Contributions and ideas are always welcome! Feel free to fork this project and submit pull requests. You can also open an issue for any suggestions or bugs.





 👨‍💻 **Author**



Pranjali Dongre

\- \[GitHub Profile](https://github.com/pranjalisdongre)

\- \[LinkedIn](https://www.linkedin.com/in/pranjali-dongre-9b291527b/)





**Note**: This project was created for educational purposes as part of a data analysis portfolio. It is not affiliated with Spotify AB.

