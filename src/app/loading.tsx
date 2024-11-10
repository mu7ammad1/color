export default function Loading() {
  return (
    <div className="hidden fixed top-0 left-0 h-1 w-full bg-[#FEED30] z-10">
      <div className="w-full h-full absolute duration-100 loader fill-mode-both"></div>
    </div>
  );
}