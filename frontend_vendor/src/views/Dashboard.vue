<template>
  <div>
    <v-toolbar app fixed clipped-left dark height="50">
      <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
      <v-toolbar-title>Application</v-toolbar-title>
    </v-toolbar>
    <v-navigation-drawer v-model="drawer" clipped hide-overlay fixed app disable-resize-watcher>
      <v-list dense>
        <v-list-tile @click>
          <v-list-tile-action>
            <v-icon>dashboard</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Dashboard</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
        <v-list-tile @click>
          <v-list-tile-action>
            <v-icon>settings</v-icon>
          </v-list-tile-action>
          <v-list-tile-content>
            <v-list-tile-title>Settings</v-list-tile-title>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </v-navigation-drawer>
    <v-container class="overall" fluid grid-list-xl text-xs-center>
      <div class="top row">
        <v-layout v-if="pageNo==1" class="layout">
          <v-flex v-for="order in firstPageFirstRowOrders" v-bind:key="order.orderNum" xs6>
            <DoubleCard :orderNum="order.orderNum" :meals="order.meals" />
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
  </div>
</template>


<script>
import SingleCard from "../components/SingleCard";
import DoubleCard from "../components/DoubleCard";

export default {
  components: {
    SingleCard,
    DoubleCard
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
    drawer: 0,
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
            foodDescription: ["Filet Burger", "Medium Fries"]
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
        ]
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
        ]
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
        ]
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
        ]
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
        ]
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
        ]
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
  height: calc(50% - (50px / 2));
}

.top {
  top: 50px;
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
