<template>
    <div class="container mt-5">
      <h2 class="text-center mb-4">Buscar Operadoras de Saúde</h2>
  
      <div class="input-group mb-3">
        <input
          type="text"
          class="form-control"
          placeholder="Digite o nome da operadora"
          v-model="query"
          @keyup.enter="buscar"
        />
        <button class="btn btn-primary" @click="buscar">Buscar</button>
      </div>
  
      <div v-if="resultado.length" class="mt-4">
        <h5 class="mb-3">Resultados:</h5>
        <ul class="list-group">
          <li v-for="(op, index) in resultado" :key="index" class="list-group-item">
            <strong>{{ op.razao_social }}</strong>
            <span class="text-muted"> - {{ op.uf }} - {{ op.modalidade }}</span>
          </li>
        </ul>
      </div>
  
      <div v-else-if="buscou" class="alert alert-warning mt-4">
        Nenhuma operadora encontrada.
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        query: "",
        resultado: [],
        buscou: false
      };
    },
    methods: {
      async buscar() {
        if (!this.query.trim()) return;
  
        try {
          const res = await fetch(`http://127.0.0.1:8000/operadoras?q=${this.query}`);
          const data = await res.json();
          this.resultado = data;
          this.buscou = true;
        } catch (error) {
          console.error("Erro ao buscar operadoras:", error);
        }
      }
    }
  };
  </script>
  