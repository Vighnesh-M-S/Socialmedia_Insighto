# README.md
# Facebook Insights Microservice

## Setup Instructions
1. **Clone the Repository:**  
   ```bash
   git clone <repo-url>
   cd facebook_insights_microservice
   ```

2. **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup MongoDB and Redis:**  
   - Install MongoDB and Redis locally.
   - Ensure MongoDB runs on `localhost:27017` and Redis on `localhost`.

4. **Run the Application:**  
   ```bash
   uvicorn app.main:app --reload
   ```

5. **API Endpoints:**  
   - `POST /scrape/{username}` - Scrapes and stores Facebook page data.
   - `GET /page/{username}` - Retrieves page data from DB.
   - `GET /posts/{username}` - Fetches recent posts.

6. **Environment Variables:**  
   Update `.env` for custom MongoDB and Redis configurations.
