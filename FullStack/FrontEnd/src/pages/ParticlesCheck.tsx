// import { useCallback } from "react";
// import Particles from "react-particles";
// //import { loadFull } from "tsparticles"; // if you are going to use `loadFull`, install the "tsparticles" package too.
// import { loadSlim } from "tsparticles-slim"; // if you are going to use `loadSlim`, install the "tsparticles-slim" package too.

// const ParticlesCheck = () => {
//     const particlesInit = useCallback(async (engine: any) => {
//         console.log(engine);
//         // you can initiate the tsParticles instance (engine) here, adding custom shapes or presets
//         // this loads the tsparticles packsage bundle, it's the easiest method for getting everything ready
//         // starting from v2 you can add only the features you need reducing the bundle size
//         //await loadFull(engine);
//         await loadSlim(engine);
//     }, []);

//     const particlesLoaded = useCallback(async (container: any) => {
//         await console.log(container);0
//     }, []);

//     return (
//         <Particles id="tsparticles" url="http://foo.bar/particles.json" init={particlesInit} loaded={particlesLoaded} />
//     );
// };

// export default ParticlesCheck;
