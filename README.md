# 🎬 Movie Recommender System (Streamlit + Hybrid AI)

![Status](https://img.shields.io/badge/Status-In%20Development-orange?style=flat) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) ![LightFM](https://img.shields.io/badge/LightFM-000000?style=flat&logo=ai&logoColor=white) ![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)

---

## 📖 About  

**Movie Recommender System** is an AI-powered application that demonstrates the concept of **hybrid recommendation systems**, combining **content-based** and **collaborative filtering** methods.  
It allows users to interactively explore movie recommendations using a **Streamlit** interface with dropdowns for genre, rating, and other parameters.  

The system will be trained using the **MovieLens 25M Dataset** from Kaggle, containing over **25 million movie ratings**.  

---

## 🚀 Features  

- 🎥 **Interactive UI:** Select genres, rating ranges, or release years and get instant recommendations.  
- 🧠 **Hybrid Recommender:** Combines content-based and collaborative filtering for improved accuracy.  
- ⚡ **Streamlit Front-End:** Simple, visual, and intuitive for demonstration or educational use.  
- 🐍 **Python-Powered:** Built using pandas, numpy, scikit-learn, and LightFM.  
- 🐳 **Dockerized Setup:** Run everything in one container for easy deployment.  

---

## 🛠️ Technologies  

| Layer | Technology |
|--------|-------------|
| **Front-End** | [Streamlit](https://streamlit.io/) |
| **Machine Learning** | [LightFM](https://making.lyst.com/lightfm/docs/home.html), [Scikit-learn](https://scikit-learn.org/) |
| **Data** | [MovieLens 25M Dataset](https://www.kaggle.com/datasets/grouplens/movielens-25m-dataset) |
| **Deployment** | [Docker](https://www.docker.com/) |
| **Data Processing** | [Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/) |

---

## ⚙️ How to Run  

### 🧰 Requirements  
- Python 3.10+  
- Docker (optional, recommended)  

### 📥 Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/luisstarlino/Movie-Recommender-System
   cd movie-recommender
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

### ▶️ Run Locally  
Run the Streamlit app:  
```bash
streamlit run app/app.py
```  
Then open your browser at: [http://localhost:8501](http://localhost:8501)

---

## 🐳 Run with Docker  

Build and run the container:  
```bash
docker build -t movie-recommender .
docker run -p 8501:8501 movie-recommender
```  

Access the application at: [http://localhost:8501](http://localhost:8501)

---

## 📂 Project Structure  

```
movie-recommender/
│
├── app/
│   ├── app.py              # Streamlit main application
│   ├── recommender.py      # Core recommendation logic
│   ├── data_loader.py      # Dataset loading and preprocessing
│   └── mock_data.py        # Temporary data for demo/testing
│
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker build configuration
└── README.md               # Documentation
```

---

## 📊 Example  

Example of mock recommendation output:  
```
🎬 Based on your preferences:
1. The Dark Knight (Action)
2. Inception (Sci-Fi)
3. Mad Max: Fury Road (Adventure)
```  

---

## 🧠 Next Steps  

- [ ] Integrate MovieLens 25M real dataset  
- [ ] Train hybrid model with LightFM  
- [ ] Add caching and user session handling  
- [ ] Improve UI with poster images and descriptions  

---

## ✨ Contributions  

Contributions are welcome!  
1. Fork this repository.  
2. Create a new branch: `git checkout -b my-feature`.  
3. Commit your changes and push: `git push origin my-feature`.  
4. Open a Pull Request.  

---

## 📄 License  

This project is licensed under the **MIT License**.  

---

## 🛡️ Contact  

For questions or suggestions, reach out:  
**Luis Guilherme**  
📧 [luis.guilherme009@gmail.com](mailto:luis.guilherme009@gmail.com)  
💼 [LinkedIn](https://www.linkedin.com/in/luis-starlino/)  
