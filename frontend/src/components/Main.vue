<template>
    <form action="" method="POST">
      <div>
      <h1>Questions</h1>
      <ul v-if="questions.length">
   
        <li v-for="question in questions" :key="question.id" class="question">
          <div v-if="question.id == (currentQuestion+1)">
          <h2>{{ question.question }}</h2>
          <ul>
            <li v-for="op in question.options" :key="op" class="option" @click="handelOptionClick">
              <input type="radio" :value="op" :id="op" :name="`question-${question.id}-answer`">
              <label :for="op">{{ op }}</label>
            </li>
          </ul>
        </div>
        </li>
      </ul>
      <div v-if="currentQuestion >= questions.length">
        thanks for filling the form, you can submit your answers now
      </div>
      <button v-if="currentQuestion == questions.length" type="submit" @click="sendAnswers">Submit</button>
    </div>
    </form>
  
  </template>
  
  
  <script>

  import axios from 'axios';
  
  export default {
    name: 'FormMain',
    data() {
      return {
        questions : [],
        answers: [],
        currentQuestion: 0
      }
    },
    mounted() {
    axios.get("http://127.0.0.1:8000/api/questions")
    .then(res => this.questions =  res.data)
    
  },
  methods: {
    sendAnswers(e) {
      e.preventDefault()
      const inputAnswers = document.querySelectorAll("input[type=radio]:checked");
 
      inputAnswers.forEach((inputAnswer, index )=> {
        this.answers.push({question : index + 1,answer : inputAnswer.value})
      })

      axios.post('http://127.0.0.1:8000/api/answers/create/',  this.answers )
      .then(res => console.log(res))
      .catch(err => {
        console.log(err)
      })
    }, 
    handelOptionClick() {
      this.currentQuestion ++ 
    }
  }
  }
  </script>
  