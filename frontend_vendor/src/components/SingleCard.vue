<template>
  <v-card class="card" dark height="100%">
    <div class="order-num">{{ orderNum }}</div>
    <hr />
    <SingleOrder
      v-for="order in orders"
      v-bind:key="order.id"
      :foodTitle="order.foodTitle"
      :foodDescription="order.foodDescription"
      :cardColor="colorList[order.id%3]"
    />
  </v-card>
</template>

<script>
import SingleOrder from "./SingleOrder";
export default {
  components: {
    SingleOrder
  },
  data: () => ({
    orderNum: "#123",
    orders: [
      {
        id: 0,
        foodTitle: "Filet Meal",
        foodDescription: ["Filet Burger", "Medium Sprite", "Medium Fries"]
      },
      {
        id: 1,
        foodTitle: "Filet Meal",
        foodDescription: ["Filet Burger", "Medium Sprite", "Medium Fries"]
      },
      {
        id: 2,
        foodTitle: "Filet Meal",
        foodDescription: ["Filet Burger", "Medium Sprite", "Medium Fries"]
      },
      {
        id: 3,
        foodTitle: "Filet Meal",
        foodDescription: ["Filet Burger", "Medium Sprite", "Medium Fries"]
      }
    ],
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

