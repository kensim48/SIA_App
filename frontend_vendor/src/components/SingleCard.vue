<template>
  <v-card dark height="100%">
    {{ orderNum }}
    <hr />
    <SingleOrder :foodTitle="foodTitle" :foodDescription="foodDescription"/>
  </v-card>
</template>

<script>
import SingleOrder from "./SingleOrder"
export default {
  components: {
    SingleOrder
  },
  data: () => ({
    orderNum: "123",
    foodTitle: "Filet Meal",
    foodDescription: ["Filet Burger", "Medium Sprite", "Medium Fries"]
  })
};
</script>
