<template>
  <div class="overall">
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex v-for="(menuItem, index) in menuItems" :key="index" xs2>
          <v-card @click.native="itemDialog=true" dark color="primary">
            <v-img src="https://cdn.vuetifyjs.com/images/cards/desert.jpg" aspect-ratio="2.75"></v-img>
            <v-card-text class="px-0">{{menuItem.title}}</v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <v-layout row justify-center>
      <v-dialog v-model="itemDialog" width="1000px">
        <v-card>
          <v-card-title>
            <span class="headline">{{menuItems[selectedItem].title}}</span>
          </v-card-title>
          <div v-for="(question, indexQn) in menuItems[selectedItem].questions" :key="indexQn">
            <div v-if="question.type==0">
              {{ question.title }}
              {{ question.description }}
              <!-- description not showing -->
              <v-flex v-for="(option, indexOp) in question.options" :key="indexOp" xs12 sm6 md3>
                <v-text-field
                  v-model="menuItems[selectedItem].questions[indexQn].options[indexOp]"
                  :label="indexOp+1"
                  class="option-text"
                ></v-text-field>
                <v-btn fab dark small @click="menuItems[selectedItem].questions[indexQn].options.splice(indexOp,1)" color="primary" class="option-button">
                  <v-icon dark>remove</v-icon>
                </v-btn>
              </v-flex>
            </div>
          </div>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="green darken-1" flat="flat" @click="itemDialog = false">Disagree</v-btn>
            <v-btn color="green darken-1" flat="flat" @click="itemDialog = false">Agree</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
  </div>
</template>

<script>
export default {
  data: () => ({
    itemDialog: false,
    selectedItem: 0,
    menuItems: [
      {
        title: "asdasd",
        description: "asdasdddsczxc",
        questions: [
          {
            type: 0,
            title: "what drink do you want",
            options: ["coke", "sprite", "7-up"]
          }
        ]
      },
      {
        title: "asdasd"
      },
      {
        title: "asdasd"
      },
      {
        title: "asdasd"
      },
      {
        title: "asdasd"
      },
      {
        title: "asdasd"
      },
      {
        title: "asdasd"
      },
      {
        title: "asdasd"
      }
    ]
  })
};
</script>


<style scoped>
.overall {
  padding-top: 50px;
}
.option-text {
float: left;
}
.option-button {
  float: right;
}
</style>
