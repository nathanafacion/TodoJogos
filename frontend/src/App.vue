<template>
  <div id="app">
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: 'Open Sans', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #32a883;
  width:100%;
  height:100%;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}

#headerTodo {
  background-color: #32a883;
}

.btn-color {
  background-color: #1c4b99;
}


.card_border {
  border:0;
  margin-top: 40px; 
  margin-bottom: 50px;
}

.card_mod {
  background-color: #32a883; 
  border:0; color: white; 
  margin-top: 20px; 
  margin-bottom: 10px;
}

.card_title_mod {
  font-size: 90px;
  font-family: Arial;
  font-weight: bold;
}

.card_header_mod {
  background-color: #1c4b99;
}

.card_title_todo_mod {
  font-size: 24px;
  font-family: Arial;
  font-weight: bold;
  color: white;
}

.check_mod {
  text-align: left;
  margin-bottom: 10px
}

.group_mod {
  margin-bottom: 10px;
}

.font_awesome_mod {
  color: white;
}
</style>