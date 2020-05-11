<template>
  <div id='raw-api'>
    <!-- <a href="/api/random">Random</a> -->
    <el-card :body-style="{ padding: '0px'}" shadow="hover">
        <img v-bind:src="pic_url"/>
    </el-card>

    <img v-for="(item, index) of this.pic_urls" 
    :key="index"
    :src="$globals.api_url +'/' + item + '?id=' + Math.random()"/>
    <p>Result: {{res}}</p>
    <el-button value='random' @click="getRes('/random')">Random</el-button>
    <el-button value='pic' @click="function(){pic_url = $globals.api_url  + '/random_img' + '?id=' + Math.random()}">RandomPicture</el-button>
    <el-button value='test' @click="function(){pic_url = $globals.api_url  + '/test_img' + '?id=' + Math.random()}">TestPicture</el-button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
    data(){
        return {
            res: 0,
            pic_url: '',
            pic_urls: []
        }
    },
    methods: {
        getRes(api) {
            axios.get(this.$globals.api_url + api).then(response => {
                this.res = response.data
                console.log(this.res)
                console.log('zykk')
            }).catch(error => {
                console.log(error)
                console.log('ErrorZYK')
            })
        },
        getImages() {
            axios.get(this.$globals.api_url + '/random_imgs').then(response => {
                this.pic_urls = response.data
                console.log(this.pic_urls)
            }).catch(error => {
                console.log(error)
            })
        },
    }
    
}
</script>

<style scoped>
.box-card {
    width: 480px;
  }

</style>