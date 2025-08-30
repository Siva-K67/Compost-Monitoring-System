install.packages("magick")
library(magick)
library(imager)
library(showimage)


# Read and display an image
image <- load.image("C:/Users/Sasirekha GVK/Downloads/Day31_23rd_May.jpeg")  # For JPEG images

gray_image <- grayscale(image)
print(gray_image)
#grid::grid.raster(gray_image)



# Compute the histogram of pixel intensities
hist_data <- hist(gray_image, plot = FALSE)
#print(hist_data)

# Normalize the histogram (divide counts by total number of pixels)
normalized_counts <- hist_data$counts / sum(hist_data$counts)
print(normalized_counts)

print(hist_data$mids)

# Plot the normalized histogram
#plot(hist_data$mids, normalized_counts, type = "h", col = "blue", 
# xlab = "Pixel Intensity", ylab = "Normalized Frequency",
 #  main = "Normalized Histogram of Image")


plot(hist_data$mids, normalized_counts, type = "h", col = "gray", 
 xlab = "Pixel Intensity", ylab = "Normalized Frequency",
   main = "Normalized Histogram of Image", lwd=15)


# Extract histogram values
intensity_values <- hist_data$mids  # Intensity levels (midpoints of bins)
frequency <- hist_data$counts       # Frequency of each intensity level

# Normalize the frequency to get probabilities
probabilities <- frequency / sum(frequency)

# Calculate mean
mean_intensity <- sum(intensity_values * probabilities)

# Calculate variance
variance_intensity <- sum((intensity_values - mean_intensity)^2 * probabilities)

# Print results
cat("Mean Intensity:", mean_intensity, "\n")
cat("Variance of Intensity:", variance_intensity, "\n")

#show_image(gray_image)

red_channel <- R(image)
green_channel <- G(image)
blue_channel <- B(image)

# Plot histograms for each channel
par(mfrow = c(1, 3))  # Arrange plots in a single row
#hist(red_channel, main = "Red Channel", xlab = "Intensity", col = "red", breaks = 50)
#hist(green_channel, main = "Green Channel", xlab = "Intensity", col = "green", breaks = 50)
#hist(blue_channel, main = "Blue Channel", xlab = "Intensity", col = "blue", breaks = 50)




