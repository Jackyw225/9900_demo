<!--
 * @Author: daidai
 * @Date: 2022-03-01 09:16:22
 * @LastEditors: Please set LastEditors
 * @LastEditTime: 2022-09-29 15:12:34 
 * @FilePath: \web-pc\src\pages\big-screen\components\item-wrap\item-wrap.vue
-->
<template>
  <dv-border-box-1 class="lr_titles" backgroundColor="#0b131d99" >
    <div class="item_title" v-if="title !== ''">
      <span class="title-inner"> &nbsp;&nbsp;{{ title }}&nbsp;&nbsp; </span>
      <dv-decoration-10 :color="['#146da0']" style="width:100%;height:10px;" />
    </div>
    <div
      :class="title !== '' ? 'item_title_content' : 'item_title_content_def'"
    >
      <slot></slot>
    </div>
  </dv-border-box-1>
</template>

<script>
export default {
  data() {
    return {};
  },
  props: {
    title: {
      type: String,
      default: () => "",
    },
  },
  created() {},

  mounted() {},
  methods: {},
};
</script>
<style lang='scss' scoped>
$item-title-height: 30px;
$item_title_content-height: calc(100% - 65px);

.lr_titles {
  height: 0px;
  box-sizing: border-box;

:deep(.border-box-content)  {
    box-sizing: border-box;
    padding: 6px 16px 0px; 

  }

  .item_title {
    height: $item-title-height;
    line-height: $item-title-height;
    margin-bottom: 10px;
    width: 100%;
    padding-top: 5px;
    color: #31abe3;
    font-family: MicrosoftYaHei-Bold;
    font-size: 18px;
    font-weight: normal;
    font-stretch: normal;
    text-align: left;
    flex-wrap: wrap;
    position: relative;
    display: flex;
    align-items: center;
    // justify-content: center;

    .zuo,
    .title-inner {
      font-weight: 900;
      letter-spacing: 2px;
      background: linear-gradient(
        92deg,
        #0072ff 0%,
        #00eaff 48.8525390625%,
        #01aaff 100%
      );
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }
  }

  .item_title_content {
    
    height: $item_title_content-height;
    // :deep(.dv-scroll-board){
    //   height: 100%;
    //   margin-top: 2%;
    // }
  }

  .item_title_content_def {
    width: 100%;
    height: 100%;
  }
}
</style>