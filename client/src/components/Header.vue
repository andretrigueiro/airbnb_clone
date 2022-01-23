<template>
    <div id="header" class="container">
      <div class="row">
        <div id="nav">
            <router-link to="/">Home</router-link> |
            <router-link to="/GuestUser">Quero me hospedar</router-link> |
            <router-link to="/HostUser">Quero hospedar alguém</router-link> |
            <router-link to="/about">Procurando algo?</router-link> |
            <router-link to="/about">Log in</router-link>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Header',
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
