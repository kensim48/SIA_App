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
  </v-container>
</template>

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
}

.layout {
  height: 100%;
}
</style>

<script>
import SingleCard from "../components/SingleCard";

export default {
  components: {
    SingleCard
  }
};
</script>

