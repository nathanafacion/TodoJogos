<template>

<div class="container">
  <div class="row">
    <div class="col-sm-12">
        <div class="card card_mod">
          <div class="card-body">
            <h1 class="card-title card_title_mod">TODO: JOGOS</h1>
          </div>
        </div>
    </div>
  </div>
  <div class="row">
    <div class="col-sm-4">
      <div class="card card_border">
        <div class="card-header card_header_mod">
            <h3 class="card-title card_title_todo_mod">COMPRAR</h3>
        </div>
        <div class="card-body">
          <div class="input-group mb-3 group_mod">
            <input id="addComprar" type="text" v-model="addComprar" name="addComprar" class="form-control" placeholder="Jogos que comprarei..." aria-label="Comprar" aria-describedby="basic-addon1" v-on:keyup="insertComprar">
          </div>
          <div v-for="(jogo, index) in jogos" :key="index">
            <div v-if="jogo.type ==='C'" class="form-check check_mod">
              <div class="row">
                <div class="col-sm-10">
                    <input class="form-check-input" type="radio" name="comprar" aria-label="..."  v-on:change="updateType(jogo,'J')"> 
                        {{jogo.title}}              
                </div>
                <div class="col-sm-2">  
                     <button class="btn btn-color btn-sm" v-on:click="removeJogo(jogo.id)" > <font-awesome-icon :icon="removeIcon" class="font_awesome_mod"/></button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-sm-4">
      <div class="card card_border">
        <div class="card-header card_header_mod">
           <h3 class="card-title card_title_todo_mod">JOGAR</h3>
        </div>
        <div class="card-body">
          <div class="input-group mb-3 group_mod">
            <input type="text" v-model="addJogar" class="form-control" placeholder="Jogos que jogarei..."  aria-label="Jogar" aria-describedby="basic-addon1" v-on:keyup="insertJogar">
          </div>
          <div v-for="(jogo, index) in jogos" :key="index">
            <div v-if="jogo.type ==='J'" class="form-check check_mod">
              <div class="row">
                <div class="col-sm-10">
                  <input class="form-check-input" type="radio" name="jogarei" v-on:change="updateType(jogo,'F')" aria-label="..."> 
                     {{jogo.title}} 
                </div>
                <div class="col-sm-2">  
                    <button class="btn btn-color btn-sm" v-on:click="removeJogo(jogo.id)" ><font-awesome-icon  :icon="removeIcon" class="font_awesome_mod"/></button>
                  
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="col-sm-4">
      <div class="card card_border">
        <div class="card-header card_header_mod">
          <h3 class="card-title card_title_todo_mod">FINALIZADOS</h3>
        </div>
        <div class="card-body">
          <div class="input-group mb-3 group_mod">
            <input type="text" v-model="addFinalizados" id="addFinalizados" name="addFinalizados" class="form-control" placeholder="Jogos que finalizei..." aria-label="Finalizados" aria-describedby="basic-addon1" v-on:keyup="insertFinalizados">
          </div>
          <div v-for="(jogo, index) in jogos" :key="index">
            <div  v-if="jogo.type ==='F'" class="form-check check_mod">
                <div class="row">
                  <div class="col-sm-10">
                      {{jogo.title}} 
                  </div>
                <div class="col-sm-2">  
                   <button class="btn btn-color btn-sm" v-on:click="removeJogo(jogo.id)" ><font-awesome-icon :icon="removeIcon" class="font_awesome_mod"/></button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>  
 </template>


<script>
import axios from "axios";
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faTimes } from '@fortawesome/free-solid-svg-icons'
export default {
  data() {
      return {
        jogos: [],
        removeIcon: faTimes,
        addComprar: null,
        addFinalizados: null,
        addJogar: null
      }
  },
  methods: {
    getJogos() {
      const path = "http://127.0.0.1:5000/jogos";
      axios
        .get(path)
        .then(res => {
          this.jogos = res.data.jogos;
        })
        .catch(error => {
          console.error(error);
        });
    },
    insert(payload,e){
      if (e.keyCode === 13 || e == 'updateType') {
        const path = "http://localhost:5000/jogos";
        axios
          .post(path, payload)
          .then(() => {
            this.getJogos();
          })
            .catch(error => {
            console.log(error);
            this.getJogos();
          });
         
      } 
    },

    removeJogo(id){
      const path = `http://localhost:5000/jogos/${id}`;
      axios
        .delete(path)
        .then(() => {
          this.getJogos();
        })
        .catch(error => {
          console.error(error);
          this.getJogos();
        });

    },

    insertComprar(e) {
      const payload = {
        title: this.addComprar,
        type: 'C',

      };
      this.insert(payload,e)
      if (e.keyCode === 13){
        this.addComprar = null
      }


    },

    insertJogar(e) {
      const payload = {
        title: this.addJogar,
        type: 'J',

      };
      this.insert(payload,e)
      if (e.keyCode === 13){
        this.addJogar = null
      }
    },

    insertFinalizados(e) {
      const payload = {
        title: this.addFinalizados,
        type: 'F',

      };
      this.insert(payload,e)
      if (e.keyCode === 13){
        this.addFinalizados = null
      }

    },

    updateType(j, type){
      const jogo = j
      this.removeJogo(j.id)
      const payload = {
        title: jogo.title,
        type: type,

      };
      this.insert(payload,'updateType')
    }
   
  },
   components: {
    FontAwesomeIcon
  },
  created() {
    this.getJogos();
  }
};
</script>