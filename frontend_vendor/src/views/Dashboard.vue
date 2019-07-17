<template>
  <v-container class="overall" grid-list-xl text-xs-center>
    <div class="top row">
      <v-layout class="layout">
        <v-flex xs6>
          <SingleCard />
        </v-flex>
        <v-flex xs6>
          <SingleCard />
        </v-flex>
      </v-layout>
    </div>
    <div class="bottom row">
      <v-layout class="layout">
        <v-flex xs4>
          <SingleCard />
        </v-flex>
        <v-flex xs4>
          <SingleCard />
        </v-flex>
        <v-flex xs4>
          <SingleCard />
        </v-flex>
      </v-layout>
    </div>
    <div class="buttons">
      <v-btn v-on:click="pageLeft()" dark large>
        <v-icon dark large>arrow_left</v-icon>
      </v-btn>
      {{ pageNo }}
      <v-btn v-on:click="pageRight()" dark large>
        <v-icon dark large>arrow_right</v-icon>
      </v-btn>
    </div>
  </v-container>
</template>


<script>
import SingleCard from "../components/SingleCard";

export default {
  components: {
    SingleCard
  },
  data: () => ({
    pageNo: 1,
    maxPages: 6
  }),
  methods: {
    pageRight() {
      console.log("right");
      this.pageNo<this.maxPages?this.pageNo++:console.log("fail");
    },
    pageLeft() {
      this.pageNo>1?this.pageNo--:null;
    }
  }
};
</script>

<style scoped>
.overall {
  height: 100%;
  background-color: brown;
}

.row {
  position: fixed;
  left: 0;
  right: 0;
  height: 50%;
}

.top {
  top: 0;
  background-color: orange;
}

.bottom {
  bottom: 0;
  background-color: green;
  padding-bottom: 3rem;
}

.layout {
  height: 100%;
}

.buttons {
  position: fixed;
  bottom: 0;
  display: inline-block;
  font-size: 2rem;
  /* width: 400px; */
  /* left: 45%; */
  /* width: 75%; */
}
</style>
