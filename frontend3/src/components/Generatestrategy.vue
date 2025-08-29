<script>
import axios from 'axios';

export default {
  data() {
    return {
      formdata: {
        business_type: "",
        budget: "", 
        target_audience: "",
        productdescription: "",
        strategy: "" 
      },
      error: ""
    }
  },
 computed: {
    renderedStrategy() {
      return marked(this.formdata.strategy || "");
    }
  },
  methods: {
    senddata() {
      axios.post('https://project-ai-umxu.onrender.com/api/generatestrategy', JSON.stringify(this.formdata), {
        headers: {
          "Content-Type": "application/json",
          "Access-Control-Allow-Origin": "*"
        }
      })
      .then(res => {
        this.formdata.strategy = res.data.strategy;
      })
      .catch(err => {
        this.error = err.response?.data?.message || "Generation failed";
      });
    }
  }
}
</script>

<template>
  <h1 class="display-4 text-center text-decoration-underline">Digital Marketing Strategy Generator</h1>
  
  <div class="container">
    <div class="main-layout">
      <!-- Form Section -->
      <div class="form-section">
        <div class="login_form">
          <h2 style="padding-bottom: 20px; text-align:center">Enter Details</h2>

          <form @submit.prevent="senddata">
            <div class="mb-3">
              <label for="business_type" class="form-label">Business Type</label>
              <input type="text" class="form-control" v-model="formdata.business_type" id="business_type" placeholder="Specify your industry or expertise" required>
            </div>
            
            <div class="mb-3">
              <label for="budget" class="form-label">Budget</label>
              <textarea type="text" class="form-control" v-model="formdata.budget" id="budget" placeholder="Tell us about your budget in detail" required></textarea>
            </div>
            
            <div class="mb-3">
              <label for="target_audience" class="form-label">Target Audience</label>
              <textarea type="text" class="form-control" v-model="formdata.target_audience" id="target_audience" placeholder="Your Customer Persona" required></textarea>
            </div>
            
            <div class="mb-3">
              <label for="product_description" class="form-label">Describe what you want to sell</label>
              <textarea type="text" class="form-control" v-model="formdata.productdescription" id="product_description" placeholder="Describe About your product or service" required></textarea>
            </div>

            <div style="text-align: center; padding:15px">
              <button type="submit" class="btn btn-success">Generate Strategy</button>
            </div>

            <p v-if="error" style="text-align: center; color: red;">{{ error }}</p>
          </form>
        </div>
      </div>

      <!-- Strategy Section -->
      <div class="strategy-section">
        <div class="strategy">
          <h2 style="padding-bottom: 20px; text-align:center">Generated Strategy</h2>
          <div class="mb-3">
            <label for="strategy_output" class="form-label">Strategy</label>
            <textarea 
              class="form-control" 
              v-model="formdata.strategy" 
              id="strategy_output" 
              rows="20"
              placeholder="Your generated strategy will appear here..."
              >
            </textarea>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.main-layout {
  display: flex;
  gap: 20px;
  justify-content: center;
  align-items: flex-start;
  margin-top: 20px;
}

.form-section {
  flex: 0 0 auto;
  margin-left: -200px;
}

.strategy-section {
  flex: 1;
  max-width: 600px;
  
}

.login_form {
  border: 1px solid grey;
  padding: 20px;
  min-height: 600px;
  width: 500px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  margin-left: 0%;
  
}

.strategy {
  border: 1px solid grey;
  padding: 20px;
  min-height: 400px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  height: 600px;
  margin-left: 10%;
}

.strategy textarea {
  resize: vertical;
  min-height: 200px;
  height: 400px;
}

/* Responsive design */
@media (max-width: 768px) {
  .main-layout {
    flex-direction: column;
    align-items: center;
  }
  
  .login_form {
    width: 100%;
    max-width: 400px;
  }
  
  .strategy-section {
    width: 100%;
    max-width: 400px;
    height: 500px;
  }
}

/* Form styling improvements */
.form-label {
  font-weight: 600;
  color: #333;
}

.form-control {
  border-radius: 4px;
  border: 1px solid #ddd;
  padding: 10px;
}

.form-control:focus {
  border-color: #28a745;
  box-shadow: 0 0 0 0.2rem rgba(40, 167, 69, 0.25);
}

.btn-success {
  background-color: #28a745;
  border-color: #28a745;
  padding: 10px 30px;
  font-weight: 600;
  border-radius: 4px;
}

.btn-success:hover {
  background-color: #218838;
  border-color: #1e7e34;
}
</style>