<template>
    <div id="footer" class="container">
      <div class="row">

        <b-list-group horizontal class="right-side">
          <b-list-group-item>© 2022 Airbnb, Inc.</b-list-group-item>
          <b-list-group-item>·</b-list-group-item>
          <b-list-group-item>Privacidade</b-list-group-item>
          <b-list-group-item>·</b-list-group-item>
          <b-list-group-item>Termos</b-list-group-item>
          <b-list-group-item>·</b-list-group-item>
          <b-list-group-item>Informações da empresa</b-list-group-item>
        </b-list-group>

        <b-list-group horizontal class="left-side">
          <b-list-group-item>
            <a href="https://www.facebook.com/Airbnb" target="_blank" rel="noopener">
              <b-icon-facebook variant="secondary"></b-icon-facebook>
            </a></b-list-group-item>
          <b-list-group-item>
            <a href="https://twitter.com/airbnb" target="_blank" rel="noopener">
              <b-icon-twitter variant="secondary"></b-icon-twitter>
            </a>
          </b-list-group-item>
          <b-list-group-item>
            <a href="https://www.instagram.com/airbnb/" target="_blank" rel="noopener">
              <b-icon-instagram variant="secondary"></b-icon-instagram>
            </a>
          </b-list-group-item>
        </b-list-group>

      </div>
    </div>
</template>

<script>
export default {
  name: 'Footer',
};
</script>
