<template>
  <div>
    <input v-model="termo" placeholder="Buscar operadora..." />
    <button @click="buscar">Buscar</button>
    
    <ul>
      <li v-for="op in operadoras" :key="op.id">
        {{ op.razao_social }} - {{ op.cnpj }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      termo: "",
      operadoras: [],
    };
  },
  methods: {
    async buscar() {
      const response = await fetch(`http://localhost:5000/buscar?termo=${this.termo}`);
      this.operadoras = await response.json();
    },
  },
};
</script>
