<template>
    <mu-menu cover :open.sync="open">
        <mu-button flat>hello</mu-button>
        <mu-list slot="content">
            <mu-list-item button @click="closeMenu">
                <mu-list-item-title>Refresh</mu-list-item-title>
            </mu-list-item>
            <mu-list-item button>
                <mu-list-item-title>Send feedback</mu-list-item-title>
            </mu-list-item>
            <mu-list-item button>
                <mu-list-item-title>Settings</mu-list-item-title>
            </mu-list-item>
            <mu-list-item button>
                <mu-list-item-title>Help</mu-list-item-title>
            </mu-list-item>
            <mu-list-item button>
                <mu-list-item-title>Sign out</mu-list-item-title>
            </mu-list-item>
        </mu-list>
    </mu-menu>
</template>

<script>
export default {
  data() {
    return {
      open: false
    };
  },
  methods: {
    closeMenu() {
      this.open = !this.open;
    }
  },
};
</script>

<style scoped>
</style>
