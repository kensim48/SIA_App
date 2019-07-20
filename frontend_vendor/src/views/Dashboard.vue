<template>
  <v-container class="overall" grid-list-xl text-xs-center>
    <div class="top row">
      <v-layout v-if="pageNo==1" class="layout">
        <v-flex v-for="order in firstPageFirstRowOrders" v-bind:key="order.orderNum" xs6>
          <SingleCard :orderNum="order.orderNum" :meals="order.meals" />
        </v-flex>
      </v-layout>
      <v-layout v-else class="layout">
        <v-flex v-for="order in firstRowOrders" v-bind:key="order.orderNum" xs4>
          <SingleCard :orderNum="order.orderNum" :meals="order.meals" />
        </v-flex>
      </v-layout>
    </div>
    <div class="bottom row">
      <v-layout class="layout">
        <v-flex v-for="order in secondRowOrders" v-bind:key="order.orderNum" xs4>
          <SingleCard :orderNum="order.orderNum" :meals="order.meals" />
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
  computed: {
    firstPageFirstRowOrders: function() {
      return this.orders.slice(0, 2);
    },
    secondRowOrders: function() {
      return this.orders.slice(
        (this.pageNo - 1) * 6 + 2,
        (this.pageNo - 1) * 6 + 5
      );
    },
    firstRowOrders: function() {
      if (this.pageNo > 1) {
        return this.orders.slice(
          (this.pageNo - 2) * 6 + 5,
          (this.pageNo - 2) * 6 + 7
        );
      } else {
        return [];
      }
    }
  },
  data: () => ({
    pageNo: 1,
    maxPages: 6,
    orders: [
      {
        orderNum: "#123",
        meals: [
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
      },
      {
        orderNum: "#124",
        meals: [
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
      },
      {
        orderNum: "#125",
        meals: [
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
      },
      {
        orderNum: "#126",
        meals: [
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
      },
      {
        orderNum: "#127",
        meals: [
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
      },
      {
        orderNum: "#128",
        meals: [
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
      }
    ]
  }),
  methods: {
    pageRight() {
      console.log("right");
      this.pageNo < this.maxPages ? this.pageNo++ : console.log("fail");
    },
    pageLeft() {
      this.pageNo > 1 ? this.pageNo-- : null;
    }
  },
  mounted() {}
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
