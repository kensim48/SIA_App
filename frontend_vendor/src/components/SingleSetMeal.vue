<template>
  <v-card :color="cardColor">
    <div class="text">
      <div class="food-title">{{ foodTitle }}</div>
      <div class="food-description" v-for="item in foodDescription" v-bind:key=item.id>
          - {{item}}
      </div>
    </div>
  </v-card>
</template>

<script>
export default {
//   data: () => ({
//     foodTitle: "Filet Meal",
//     foodDescription: ["Filet Burger", "Medium Sprite", "Medium Fries"]
//   }),
  props: {
      foodTitle: String,
      foodDescription: Array,
      cardColor: String
  }
};
</script>

<style scoped>
.text{
    text-align: left;
}

.food-title{
    font-size: 1.8rem;
}

.food-description{
    font-size: 1.2rem;
}
</style>

