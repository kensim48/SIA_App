<template>
  <v-card color="blue darken-4">
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
      foodDescription: Array
  }
};
</script>

<style scoped>
.text{
    text-align: left;
}

.food-title{
    font-size: 3rem;
}

.food-description{
    font-size: 1.5rem;
}
</style>

