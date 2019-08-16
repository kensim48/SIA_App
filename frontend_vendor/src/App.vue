<template>
  <v-app>
    <div v-if="$route.name!='login'">
      <v-toolbar app fixed clipped-left dark height="50">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <v-toolbar-title>Greenup</v-toolbar-title>
      </v-toolbar>
      <v-navigation-drawer v-model="drawer" absolute
      temporary disable-resize-watcher>
        <v-list dense>
          <v-list-tile @click="routerFwd('dashboard')">
            <v-list-tile-action>
              <v-icon>dashboard</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Order Dashboard</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
          <v-list-tile @click="routerFwd('menu')">
            <v-list-tile-action>
              <v-icon>settings</v-icon>
            </v-list-tile-action>
            <v-list-tile-content>
              <v-list-tile-title>Edit Menu</v-list-tile-title>
            </v-list-tile-content>
          </v-list-tile>
        </v-list>
      </v-navigation-drawer>
    </div>

    <router-view></router-view>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: false
  }),
  components: {},
  mounted() {
    console.log(this.$route.name);
  },
  methods: {
    routerFwd(addr){
      this.$router.push(addr);
    }
  }
};
</script>
<style scoped>
</style>
