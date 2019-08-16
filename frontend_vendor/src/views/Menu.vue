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
        <v-flex xs2>
          <v-card @click.native="createNewMenuItem(menuItems.length)" dark color="grey darken-2">
            <v-img src="plus.png" aspect-ratio="2.75"></v-img>
            <v-card-text class="px-0">New menu item</v-card-text>
          </v-card>
        </v-flex>
      </v-layout>
    </v-container>
    <v-layout row justify-center>
      <v-dialog persistent v-model="itemDialog" width="600px" v-if="menuItems[selectedItem]">
        <v-card>
          <v-card-title>
            <v-text-field
              style="width: 100%;"
              v-model="menuItems[selectedItem].title"
              label="Title of meal"
              box
            ></v-text-field>
            <v-textarea
              style="width: 100%;"
              label="Description of meal"
              v-model="menuItems[selectedItem].description"
              box
            ></v-textarea>
            <v-text-field
              style="width: 100%;"
              v-model="menuItems[selectedItem].price"
              label="Price of meal"
              box
            ></v-text-field>
          </v-card-title>
          <div class="question">
            <div v-for="(question, indexQn) in menuItems[selectedItem].questions" :key="indexQn">
              <hr v-if="indexQn!=0" style="margin: 20px 0;" />
              <v-layout row wrap>
                <v-flex xs12>
                  <v-text-field
                    v-model="menuItems[selectedItem].questions[indexQn].title"
                    label="Title of question"
                    outline
                  ></v-text-field>
                  <div v-if="question.type==0">Type of qn: Select one option only</div>
                  <div v-else-if="question.type==1">
                    <v-layout row wrap>
                      <v-flex xs12>Type of qn: Select multiple options</v-flex>
                      <v-flex xs4>
                        <v-select
                          v-model="menuItems[selectedItem].questions[indexQn].optionLimits[0]"
                          :items="minMaxItems"
                          label="Minimum"
                        ></v-select>
                      </v-flex>
                      <v-flex xs2 />
                      <v-flex xs4>
                        <v-select
                          v-model="menuItems[selectedItem].questions[indexQn].optionLimits[1]"
                          :items="maxItems(indexQn)"
                          label="Maximum"
                        ></v-select>
                      </v-flex>
                      <v-flex xs2 />
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
                    small
                    @click="menuItems[selectedItem].questions[indexQn].options.splice(indexOp,1)"
                    color="primary"
                    :disabled="menuItems[selectedItem].questions[indexQn].options.length<=1"
                  >
                    <v-icon dark>remove</v-icon>
                  </v-btn>
                </v-flex>
                <v-flex xs12>
                  <v-btn
                    dark
                    @click="menuItems[selectedItem].questions[indexQn].options.push('')"
                    color="secondary"
                  >Add option</v-btn>
                </v-flex>
              </v-layout>
            </div>
          </div>

          <v-card-actions>
            <v-menu open-on-hover top offset-y>
              <template v-slot:activator="{ on }">
                <v-btn pa-2 color="primary" dark v-on="on">Add question</v-btn>
              </template>
              <v-list>
                <v-list-tile v-for="(type, index) in typesOfQuestion" :key="index" @click>
                  <v-list-tile-title @click="createNewQuestion(index)">{{ type }}</v-list-tile-title>
                </v-list-tile>
              </v-list>
            </v-menu>
            <v-spacer></v-spacer>
            <!-- <v-btn color="primary" flat="flat" @click="itemDialog = false">Cancel</v-btn> -->
            <v-btn color="primary" flat="flat" @click="cancelItem">Cancel</v-btn>
            <v-btn color="primary" flat="flat" @click="saveItem">Save</v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-layout>
  </div>
</template>

<script>
import axios from "axios";

export default {
  mounted() {
    this.getEntireMenu();
  },
  methods: {
    getEntireMenu() {
      axios.get("http://localhost:8000/vendor/MenuList/").then(response => {
        console.log(response.data);
        this.menuItems = response.data.menuItems;
        this.storeName = response.data.storeName;
        this.storeID = response.data.storeID;
      });
    },
    saveItem() {
      this.itemDialog = false;
      console.log(this.menuItems[this.selectedItem]);
      axios
        .post("http://127.0.0.1:8000/vendor/MenuList/", {
          meal: this.menuItems[this.selectedItem]
        })
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {});
    },
    cancelItem() {
      this.itemDialog = false;
      this.getEntireMenu();
    },
    createNewMenuItem(index) {
      this.selectedItem = index;
      this.itemDialog = true;
      this.menuItems.push({
        title: "",
        description: "",
        price: 0.0,
        questions: [],
        store_ID: this.storeID
      });
      console.log(this.selectedItem);
    },
    clickMenuItem(index) {
      this.selectedItem = index;
      this.itemDialog = true;
      console.log(this.menuItems[this.selectedItem]);
    },
    maxItems(indexQn) {
      return this.minMaxItems.slice(
        this.menuItems[this.selectedItem].questions[indexQn].optionLimits[0] - 1
      );
    },
    createNewQuestion(type) {
      type == 0
        ? this.menuItems[this.selectedItem].questions.push({
            type: 0,
            title: "",
            optionLimits: [null, null],
            options: [""]
          })
        : this.menuItems[this.selectedItem].questions.push({
            type: 1,
            title: "",
            optionLimits: [null, null],
            options: [""]
          });
    }
  },
  data: () => ({
    itemDialog: false,
    selectedItem: 0,
    minMaxItems: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    typesOfQuestion: ["Select one option", "Select multiple options"],
    menuItems: [],
    storeName: "",
    storeID: 0
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
  padding: 2% 8%;
}
</style>
