<template>
  <div class="overall">
    <v-container grid-list-md text-xs-center>
      <v-layout row wrap>
        <v-flex v-for="(menuItem, index) in menuItems" :key="index" xs2>
          <v-card @click.native="clickMenuItem(index)" dark color="primary">
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
          <div
            v-for="(question, indexQn) in menuItems[selectedItem].questions"
            :key="indexQn"
            class="question"
          >
            {{ question.title }}
            {{ question.description }}
            <!-- description not showing -->
            <v-layout row wrap>
              <v-flex xs3>
                <div v-if="question.type==0">(Select one)</div>
                <div v-else-if="question.type==1">
                  <v-layout row wrap>
                    <v-flex xs12>(Select multiple)</v-flex>
                    <v-flex xs5>
                      <v-select
                        v-model="menuItems[selectedItem].questions[indexQn].optionLimits[0]"
                        :items="minMaxItems"
                        box
                        label="Minimum"
                      ></v-select>
                    </v-flex>
                    <v-flex xs2 />
                    <v-flex xs5>
                      <v-select
                        v-model="menuItems[selectedItem].questions[indexQn].optionLimits[1]"
                        :items="maxItems(indexQn)"
                        box
                        label="Maximum"
                      ></v-select>
                    </v-flex>
                  </v-layout>
                </div>
              </v-flex>
              <v-flex v-for="(option, indexOp) in question.options" :key="indexOp" xs12>
                <v-text-field
                  v-model="menuItems[selectedItem].questions[indexQn].options[indexOp]"
                  :label="(indexOp+1).toString()"
                  class="option-text"
                ></v-text-field>
                <v-btn
                  fab
                  dark
                  small
                  @click="menuItems[selectedItem].questions[indexQn].options.splice(indexOp,1)"
                  color="primary"
                >
                  <v-icon dark>remove</v-icon>
                </v-btn>
              </v-flex>
              <v-flex xs12>
                <v-btn
                  dark
                  @click="menuItems[selectedItem].questions[indexQn].options.push('')"
                  color="primary"
                >add option</v-btn>
              </v-flex>
            </v-layout>
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
  methods: {
    clickMenuItem(index) {
      this.selectedItem = index;
      this.itemDialog = true;
    },
    maxItems(indexQn) {
      return this.minMaxItems.slice(
        this.menuItems[this.selectedItem].questions[indexQn].optionLimits[0] - 1
      );
    },
    computed: {}
  },
  data: () => ({
    itemDialog: false,
    selectedItem: 0,
    minMaxItems: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    menuItems: [
      {
        title: "asdasd",
        description: "asdasdddsczxc",
        questions: [
          {
            type: 1,
            optionLimits: [1, 10],
            title: "what drink do you want",
            options: ["coke", "sprite", "7-up"]
          },
          {
            type: 0,
            title: "what drink do you want",
            options: ["coke", "sprite", "7-up"]
          },
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
.question {
  display: inline;
}
</style>
