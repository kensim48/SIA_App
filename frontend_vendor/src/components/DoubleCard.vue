<template>
  <v-card class="card" dark height="100%" @click="qr_scanner()">
    <div class="order-num">{{ orderNum }}</div>
    <hr />
    <v-layout>
      <v-flex xs6 pa-1 pl-3>
        <SingleSetMeal
          v-for="(meal, index) in leftColMeals"
          v-bind:key="index"
          :foodTitle="meal.foodTitle"
          :foodDescription="meal.foodDescription"
          :cardColor="colorList[index%colorList.length]"
        />
      </v-flex>
      <v-flex xs6 pa-1 pr-3>
        <SingleSetMeal
          v-for="(meal, index) in rightColMeals"
          v-bind:key="index"
          :foodTitle="meal.foodTitle"
          :foodDescription="meal.foodDescription"
          :cardColor="colorList[(index+1)%colorList.length]"
        />
      </v-flex>
    </v-layout>
  </v-card>
</template>

<script>
import SingleSetMeal from "./SingleSetMeal";
import EventBus from "../EventBus";
export default {
  components: {
    SingleSetMeal
  },
  props: {
    orderNum: String,
    meals: Array
  },
  data: () => ({
    colorList: ["blue darken-4", "orange darken-4"]
  }),
  computed: {
    leftColMeals: function() {
      var leftMeals = [];
      for (var i = 0; i < this.meals.length; i += 2) {
        // take every second element
        leftMeals.push(this.meals[i]);
      }
      return leftMeals;
    },
    rightColMeals: function() {
      var rightMeals = [];
      for (var i = 1; i < this.meals.length; i += 2) {
        // take every second element
        rightMeals.push(this.meals[i]);
      }
      return rightMeals;
    }
  },
  methods: {
    qr_scanner() {
      EventBus.$emit('QR_SCANNER')
    }
  }
};
</script>

<style scoped>
.order-num {
  font-size: 1.2rem;
  font-weight: 500;
  position: relative;
}

.card {
  overflow-x: hidden;
  overflow-y: scroll;
}
</style>

