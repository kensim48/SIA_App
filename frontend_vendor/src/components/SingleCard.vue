<template>
  <v-card class="card" dark height="100%">
    <div class="order-num">{{ orderNum }}</div>
    <hr />
    <SingleSetMeal
      v-for="(meal, index) in meals"
      v-bind:key="index"
      :foodTitle="meal.foodTitle"
      :foodDescription="meal.foodDescription"
      :cardColor="colorList[index%colorList.length]"
    />
  </v-card>
</template>

<script>
import SingleSetMeal from "./SingleSetMeal";
export default {
  components: {
    SingleSetMeal
  },
  props: {
    orderNum: String,
    meals: Array
  },
  data: () => ({
    colorList: ["blue darken-4", "red darken-4", "green darken-4"]
  })
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

