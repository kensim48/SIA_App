<template>
  <v-app>
    <div v-if="$route.name!='login'">
      <v-toolbar app fixed clipped-left dark height="50">
        <v-toolbar-side-icon @click.stop="drawer = !drawer"></v-toolbar-side-icon>
        <v-toolbar-title>Application</v-toolbar-title>
      </v-toolbar>
      <v-navigation-drawer v-model="drawer" absolute
      temporary disable-resize-watcher>
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
  }
};
</script>
<style scoped>
</style>
