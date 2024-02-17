<!-- <template>
    <div class="wrapper">
      <div v-for="(button, key) in tableIcons" 
       :key="key"
       class="icon"
       >
        <v-btn    
          class="btn"
        >
          <v-icon v-if="button.color" color="red">{{ button.icon }}</v-icon>
          <v-icon v-else >{{ button.icon }}</v-icon>
        </v-btn>
        <span v-if="button.color" class="redText">{{ button.text }}</span>
        <span v-else >{{ button.text }}</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data(){
      return{
        tableIcons:[
          { text:"左に列追加", icon: 'mdi-table-column-plus-before' },
          { text:"右に列追加", icon: 'mdi-table-column-plus-after' },
          { text:"列削除", icon: 'mdi-table-column-remove', color: 'red' },
          { text:"下に行追加", icon: 'mdi-table-row-plus-after' },
          { text:"上に行追加", icon: 'mdi-table-row-plus-before' },
          { text:"行削除", icon: 'mdi-table-row-remove', color: 'red' },
        ],
      }
    }
  }
  </script>
  
  <style lang="scss" scoped>
    .wrapper{
      display: flex;
    }
    .icon{
      display: flex;
      flex-direction: column;
      margin-left: 10px;
      text-align: center;
    }
    .redText{
      color: red
    }
  </style> -->


<template>
    
  <v-container>
    <v-select
    :items="sizes"
    label="AAA"
    required
    >
    </v-select>

    <v-file-input label="Select a file" v-model="files" accept=".txt, .html, .pdf"
    ></v-file-input>
  </v-container>
</template>

<script>
export default {
    data() {
        return{
            sizes: ['small', 'medium', 'large'],
            files: [],
        }
    },
}
</script>