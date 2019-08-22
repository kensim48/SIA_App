<template>
  <div>
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
    <v-dialog v-model="dialog" width="500">
      <v-card>
        <v-card-title class="blue lighten-2" primary-title>Scan Container</v-card-title>

        <v-card-text>Scan reusuable container's code to notify user that the order is ready</v-card-text>
        <v-img src="GreenCap.jpg"/>
        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="dialog = false">Cancel</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>


<script>
import SingleCard from "../components/SingleCard";
import DoubleCard from "../components/DoubleCard";
import axios from "axios";
import EventBus from "../EventBus";

export default {
  components: {
    SingleCard,
    DoubleCard
  },
  mounted() {
    this.getAllOrders();
    EventBus.$on("QR_SCANNER", () => {
      this.dialog = true;
    });
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
    dialog: false,
    orders: [
      {
        orderNum: "#123",
        meals: [
          // {
          //   id: 0,
          //   orderMeal: "Filet Meal",
          //   orderDetail: ["Filet Burger", "Medium Sprite", "Medium Fries"]
          // },
          // {
          //   id: 1,
          //   orderMeal: "Filet Meal",
          //   orderDetail: ["Filet Burger", "Medium Fries"]
          // },
          // {
          //   id: 2,
          //   orderMeal: "Filet Meal",
          //   orderDetail: ["Filet Burger", "Medium Sprite", "Medium Fries"]
          // },
          // {
          //   id: 3,
          //   orderMeal: "Filet Meal",
          //   orderDetail: ["Filet Burger", "Medium Sprite", "Medium Fries"]
          // }
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
    },
    getAllOrders() {
      axios.get("http://localhost:8000/orders/OrderList/").then(response => {
        console.log(response.data);
        this.orders = response.data.orders;
        this.maxPages = Math.ceil((this.orders - 5) / 6) + 1;
        this.pageNo = this.pageNo > this.maxPages ? this.maxPages : this.pageNo;
      });
    }
  }
};
</script>

<style scoped>
.overall {
  height: 100%;
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
  background-color: lightgrey;
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
