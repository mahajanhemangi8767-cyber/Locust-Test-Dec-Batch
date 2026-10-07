from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    
    
    @task
    def health_check(self):
        self.client.get("/health")
      
        
    @task
    def home(self):
        self.client.get("/")